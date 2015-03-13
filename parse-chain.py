import os
import sys
import sip

try:
    apis = ["QDate", "QDateTime", "QString", "QTextStream",
            "QTime", "QUrl", "QVariant"]
    for api in apis:
        sip.setapi(api, 2)
except ValueError:
    # API has already been set so we can't set it again.
    pass

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from PyQt4.QtWebKit import *

from forms.parsechain import Ui_ParseChain


# noinspection PyPep8Naming
class ParseChain(QDialog, Ui_ParseChain):
    def __init__(self, parent=None):
        super(ParseChain, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        # noinspection PyArgumentList
        self.lastdir = QDir.homePath()

    def initUi(self):
        self.log.ensureCursorVisible()
        self.btnChainSelect.clicked.connect(self.setChainPath)
        self.btnParse.clicked.connect(self.parseChain)
        self.btnClear.clicked.connect(self.log.clear)
        self.btnClose.clicked.connect(self.close)
        self.resize(700, 700)

    def showRootCerts(self):
        return self.chkRootCerts.isChecked()

    def showCertBody(self):
        return self.chkBody.isChecked()

    @pyqtSlot(str)
    def appendLog(self, msg):
        self.log.append(msg + "\n")
        self.log.moveCursor(QTextCursor.Start)

    def chainPath(self):
        return self.leChainPath.text()

    @pyqtSlot()
    def setChainPath(self):
        # noinspection PyArgumentList
        f = QFileDialog.getOpenFileName(parent=self,
                                        caption="Select CA chain .pem file",
                                        directory=self.lastdir,
                                        filter="PEM (*.pem)")
        self.activateWindow()
        if f:
            self.leChainPath.setText(f)
            fi = QFileInfo(f)
            self.lastdir = fi.dir().canonicalPath()

    def _certsOutText(self, certs, sort=False):
        def _attr(tag, mthd):
            a = unicode(mthd)
            return u"- {0}: {1}\n".format(tag, a) if a else ''

        def _subj(tag, crt, enum):
            return _attr(tag, crt.subjectInfo(enum))

        cas = []
        for c in certs:
            cert = c
            """:type: QSslCertificate"""
            title = cert.subjectInfo(QSslCertificate.CommonName)
            if not title:
                title = cert.subjectInfo(QSslCertificate.OrganizationalUnitName)
            if not title:
                title = cert.subjectInfo(QSslCertificate.Organization)
            txt = u"{0}\n".format(unicode(title))
            txt += _subj("OU", cert, QSslCertificate.OrganizationalUnitName)
            txt += _subj("O", cert, QSslCertificate.Organization)
            txt += _subj("CN", cert, QSslCertificate.CommonName)
            txt += _subj("L", cert, QSslCertificate.LocalityName)
            txt += _subj("C", cert, QSslCertificate.CountryName)
            txt += _subj("ST", cert, QSslCertificate.StateOrProvinceName)

            txt += _attr(">=", cert.effectiveDate().toString())
            txt += _attr("<=", cert.expiryDate().toString())

            def sha():
                h = str(cert.digest(QCryptographicHash.Sha1).toHex())
                return' '.join(s.encode('hex') for s in h.decode('hex')).upper()
            txt += _attr("SHA1", sha())

            def issuer():
                iss = cert.issuerInfo(QSslCertificate.CommonName)
                if not iss:
                    iss = cert.issuerInfo(
                        QSslCertificate.OrganizationalUnitName)
                if not iss:
                    iss = cert.issuerInfo(QSslCertificate.Organization)
                return unicode(iss)
            issuercert = issuer()
            txt += _attr("Issuer", issuercert)

            if title == issuercert:
                txt += u"** Self-signed **\n"

            if self.showCertBody():
                txt += u"{0}".format(cert.toPem())
            cas.append(txt)
        return '' if not cas else "\n".join(sorted(cas) if sort else cas)

    @pyqtSlot()
    def parseChain(self):
        self.log.clear()
        if not self.chainPath() and not self.showRootCerts():
            return

        if not self.chainPath():
            self.appendLog("Warning: no CA chain PEM file path set")

        req = QNetworkRequest()
        sslc = req.sslConfiguration()
        """:type: QSslConfiguration"""
        rootcerts = sslc.caCertificates()

        # noinspection PyArgumentList
        if self.chainPath():
            self.appendLog("######### CA Cert(s) #########")
            cf = QFile(self.chainPath())
            data = QByteArray()
            if cf.open(QIODevice.ReadOnly | QIODevice.Text):
                data = cf.readAll()
            cf.close()
            if data.isNull():
                self.appendLog("ERROR: could not read CA chain PEM file")
                return
            # self.appendLog("------- QSslCertificate() -------")
            # cert = QSslCertificate(data)
            # self.appendLog(self._certsOutText([cert]))
            self.appendLog("--- QSslCertificate.fromData() ---")

            # noinspection PyArgumentList
            icerts = QSslCertificate.fromData(data)
            self.appendLog(self._certsOutText(icerts, sort=False))

        if self.showRootCerts():
            self.appendLog("######### Root Certs #########")
            self.appendLog(self._certsOutText(rootcerts, sort=True))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = ParseChain()
    dlg.exec_()
