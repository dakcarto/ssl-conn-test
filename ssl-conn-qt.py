import os
import sys
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from PyQt4.QtWebKit import *
from forms.testbrowser import Ui_TestBrowser


# noinspection PyPep8Naming
class TestBrowser(QDialog, Ui_TestBrowser):
    def __init__(self, authm, app=None, parent=None):
        """Constructor."""
        super(TestBrowser, self).__init__(parent)
        self.loaded = False
        self.authm = authm
        self.app = app
        """:type : QgsAuthManager"""
        self.reply = None
        """:type : QNetworkReply"""

        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.nam = self.webView.page().networkAccessManager()
        """:type : QNetworkAccessManager"""

        self.qt48 = "0x%0.2X" % QT_VERSION >= "0x40800"

        self.defaulturls = [
            "https://example.com",
            "http://localhost",
            "http://localhost:8080",
            "https://localhost:8443",
            "https://localhost:8443/geoserver/rest/workspaces.xml",
            "https://localhost:8443/geoserver/opengeo/wms?service=WMS"
            "&version=1.1.0&request=GetMap&layers=opengeo:countries&styles=&"
            "bbox=-180.0,-90.0,180.0,90.0&width=720&height=400&srs=EPSG:4326&"
            "format=application/openlayers"
        ]
        self.comboBox.lineEdit().setAlignment(Qt.AlignLeft)
        self.comboBox.addItems(self.defaulturls)

        if self.qt48:
            # Qt 4.8 defaults to SecureProtocols, i.e. TlsV1SslV3
            # http://qt-project.org/doc/qt-4.8/qssl.html#SslProtocol-enum
            self.protocols = [
                "SecureProtocols",
                "TlsV1",
                "TlsV1SslV3",
                "SslV3",
                "SslV2",
            ]
        else:
            # older Qt 4.7 defaults to now-vulnerable SSLv3
            # http://qt-project.org/doc/qt-4.7/qssl.html
            self.protocols = [
                "TlsV1",
                "SslV3",
                "SslV2",
                ]
        self.cmbxProtocol.addItems(self.protocols)

        self.plainTextEdit.ensureCursorVisible()

        self.setNamConnections()
        self.webView.linkClicked["QUrl"].connect(self.loadUrl)
        self.webView.urlChanged["QUrl"].connect(self.setLocation)
        self.webView.titleChanged[str].connect(self.updateTitle)
        self.backButton.clicked.connect(self.webView.back)
        self.forwardButton.clicked.connect(self.webView.forward)
        self.reloadButton.clicked.connect(self.webView.reload)
        self.stopButton.clicked.connect(self.webView.stop)
        self.comboBox.activated[str].connect(self.loadUrlTxt)
        self.clearButton.clicked.connect(self.clearLog)
        self.goButton.clicked.connect(self.loadCurrentUrl)
        self.sourceButton.clicked.connect(self.showPageSource)
        self.pageResetButton.clicked.connect(self.resetPage)

        self.appendLog(self.app.showSettings())

    def setNamConnections(self):
        self.nam.finished["QNetworkReply*"].connect(self.requestReply)
        self.nam.sslErrors["QNetworkReply*", "const QList<QSslError>&"] \
            .connect(self.onSslErrors)

    @pyqtSlot(str)
    def updateTitle(self, title):
        self.setWindowTitle(title)

    @pyqtSlot("QUrl")
    def setLocation(self, url):
        """
        :type url: QUrl
        """
        self.comboBox.lineEdit().setText(url.toString())

    @pyqtSlot(str)
    def appendLog(self, msg):
        self.plainTextEdit.appendPlainText(msg)
        self.plainTextEdit.moveCursor(QTextCursor.End)
        # qApp.processEvents()

    @pyqtSlot()
    def clearLog(self):
        self.plainTextEdit.clear()

    @pyqtSlot()
    def clearWebView(self):
        self.webView.setContent(QByteArray())

    @pyqtSlot()
    def loadCurrentUrl(self):
        curtxt = self.comboBox.lineEdit().text()
        if not curtxt:
            return
        self.loadUrl(QUrl(curtxt))

    @pyqtSlot(str)
    def loadUrlTxt(self, urltxt):
        if not urltxt:
            return
        self.loadUrl(QUrl(urltxt))

    @pyqtSlot("QUrl")
    def loadUrl(self, url):
        """
        :type url: QUrl
        """
        if not url or not url.isValid():
            return

        # ishttps = url.toString().startswith("https")
        https = url.scheme().lower() == "https"

        self.appendLog("### Requested: {0} ###".format(url.toString()))

        req = QNetworkRequest()
        req.setUrl(url)
        req.setRawHeader("User-Agent",
                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; "
                         "rv:32.0) Gecko/20100101 Firefox/32.0")
        if https and self.leAuthId.text():
            self.authm.updateNetworkRequest(req, self.leAuthId.text())

        if https:
            sslc = req.sslConfiguration()
            """:type: QSslConfiguration"""
            sslc.setProtocol(self.getSslProtocol())
            req.setSslConfiguration(sslc)

            sslc2 = req.sslConfiguration()
            self.appendLog("SSL connection protocol: {0}".format(
                self.getProtocolText(sslc2.protocol())))

        del self.reply
        self.reply = self.nam.get(req)

        if https and self.leAuthId.text():
            self.authm.updateNetworkReply(self.reply, self.leAuthId.text())

        self.clearWebView()
        self.setLocation(self.reply.request().url())
        self.webView.setFocus()
        self.reply.readyRead.connect(self.loadReply)

    @pyqtSlot()
    def loadReply(self):
        url = QUrl(self.reply.url())

        # handle redirects
        redirect = self.reply.attribute(
            QNetworkRequest.RedirectionTargetAttribute)
        """:type: QUrl"""
        if redirect:
            if not redirect.scheme():
                redirect = url.resolved(redirect)
            self.appendLog("### Redirected to: {0} ###"
                           .format(redirect.toString()))
            self.reply.deleteLater()
            self.loadUrl(redirect)
            return

        self.webView.setContent(self.reply.readAll(), '', url)
        self.appendLog("### Reply loaded ###\n")

        if url.path().endswith(".xml"):
            self.appendLog("XML loaded, showing page source...\n")
            # noinspection PyCallByClass,PyTypeChecker
            QTimer.singleShot(1000, self.showPageSource)

    @pyqtSlot("QNetworkReply*")
    def requestReply(self, reply):
        """
        :type reply: QNetworkReply
        """
        if reply.error() != QNetworkReply.NoError:
            self.appendLog("Network error #{0}: {1}\n"
                           .format(reply.error(), reply.errorString()))

    @pyqtSlot("QNetworkReply*", "const QList<QSslError>&")
    def onSslErrors(self, reply, errors):
        msg = "SSL errors occurred accessing URL {0}:"\
            .format(reply.request().url().toString())
        for error in errors:
            if error.error() == QSslError.NoError:
                continue
            msg += "\n" + error.errorString()
        self.appendLog(msg + "\n")

    def getSslProtocol(self):
        ptxt = self.cmbxProtocol.currentText()
        enums_kv = dict((k, v) for k, v in vars(QSsl).items()
                        if isinstance(v, QSsl.SslProtocol))
        if ptxt not in enums_kv:
            if self.qt48:
                return QSsl.SecureProtocols  # default
            else:
                return QSsl.TlsV1  # switch default from SSLv3
        return enums_kv[ptxt]

    # noinspection PyMethodMayBeStatic
    def getProtocolText(self, enumv):
        enums_vk = dict((v, k) for k, v in vars(QSsl).items()
                        if isinstance(v, QSsl.SslProtocol))
        return enums_vk[enumv]

    def resetPage(self):
        pg = QWebPage(self.webView)
        self.webView.setPage(pg)
        del self.nam
        self.nam = self.webView.page().networkAccessManager()
        self.setNamConnections()
        self.appendLog("Reset Web page and authentication cache\n")

    @pyqtSlot()
    def showPageSource(self):
        src = self.webView.page().currentFrame().documentElement().toOuterXml()
        if not src:
            self.appendLog("No Web page source to display\n")
            return
        dlg = QDialog(self)
        dlg.setWindowTitle("Page Source")
        layout = QVBoxLayout(dlg)
        pt = QPlainTextEdit(dlg)
        pt.setPlainText(src)
        layout.addWidget(pt)
        buttonbox = QDialogButtonBox(QDialogButtonBox.Close, Qt.Horizontal, dlg)
        buttonbox.rejected.connect(dlg.close)
        layout.addWidget(buttonbox)
        dlg.setLayout(layout)
        dlg.resize(700, 500)
        dlg.exec_()
        del dlg

    @pyqtSlot(int)
    def on_cmbxProtocol_activated(self, idx):
        self.resetPage()

    @pyqtSlot()
    def on_btnAuthEditor_clicked(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Authentication Configurations")
        layout = QVBoxLayout(dlg)
        ae = QgsAuthConfigEditor(dlg)
        layout.addWidget(ae)
        buttonbox = QDialogButtonBox(QDialogButtonBox.Close, Qt.Horizontal, dlg)
        buttonbox.rejected.connect(dlg.close)
        layout.addWidget(buttonbox)
        dlg.setLayout(layout)
        dlg.resize(700, 500)
        dlg.exec_()
        del dlg

    @pyqtSlot()
    def on_btnAuthSelect_clicked(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Select Authentication")
        layout = QVBoxLayout(dlg)

        asl = QgsAuthConfigSelect(dlg)
        if self.leAuthId.text():
            asl.setConfigId(self.leAuthId.text())
        layout.addWidget(asl)

        buttonbox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, dlg)
        buttonbox.accepted.connect(dlg.accept)
        buttonbox.rejected.connect(dlg.close)
        layout.addWidget(buttonbox)

        dlg.setLayout(layout)
        if dlg.exec_():
            self.appendLog("Selected authid: {0}\n".format(asl.configId()))
            self.leAuthId.setText(asl.configId())
            self.resetPage()
        del dlg

    @pyqtSlot()
    def on_clearAuthButton_clicked(self):
        self.leAuthId.clear()
        self.resetPage()


if __name__ == "__main__":

    # Instantiate standalone QGIS (no desktop GUI)
    qgsapp = QgsApplication(sys.argv, True)
    """:type : QgsApplication"""

    if not qgsapp:
        print "Failed to launch QGIS standalone app"
        sys.exit(1)

    # These are for referencing the correct QSettings for the QGIS app
    # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
    QCoreApplication.setOrganizationName('QGIS')
    # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
    QCoreApplication.setOrganizationDomain('qgis.org')
    # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
    QCoreApplication.setApplicationName('QGIS2')

    # Initialize QGIS
    qgsapp.initQgis()

    # Do some inits that are normally done on QGIS desktop app's launch
    # Instantiate the QgsCredentials singleton dialog
    # noinspection PyUnusedLocal
    creds = QgsCredentialDialog()
    # Initialize the auth system singleton
    # noinspection PyArgumentList
    authman = QgsAuthManager.instance()
    if QGis.QGIS_VERSION_INT < 20800:
        authman.init()  # init() part of initQgis() in 2.8+

    tb = TestBrowser(authman, app=qgsapp, parent=None)
    tb.exec_()
    tb.deleteLater()  # or WebKit thread crashes

    # Clean up QGIS resources
    qgsapp.exitQgis()
    sys.exit(0)
