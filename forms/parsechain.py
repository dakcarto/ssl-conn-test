# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/parsechain.ui'
#
# Created: Thu Mar 12 18:18:13 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ParseChain(object):
    def setupUi(self, ParseChain):
        ParseChain.setObjectName(_fromUtf8("ParseChain"))
        ParseChain.resize(574, 628)
        self.verticalLayout = QtGui.QVBoxLayout(ParseChain)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ParseChain)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.leChainPath = QtGui.QLineEdit(ParseChain)
        self.leChainPath.setReadOnly(True)
        self.leChainPath.setObjectName(_fromUtf8("leChainPath"))
        self.horizontalLayout_3.addWidget(self.leChainPath)
        self.btnChainSelect = QtGui.QToolButton(ParseChain)
        self.btnChainSelect.setMaximumSize(QtCore.QSize(16777215, 22))
        self.btnChainSelect.setObjectName(_fromUtf8("btnChainSelect"))
        self.horizontalLayout_3.addWidget(self.btnChainSelect)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.btnParse = QtGui.QPushButton(ParseChain)
        self.btnParse.setObjectName(_fromUtf8("btnParse"))
        self.horizontalLayout_2.addWidget(self.btnParse)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.log = QtGui.QTextEdit(ParseChain)
        self.log.setObjectName(_fromUtf8("log"))
        self.verticalLayout.addWidget(self.log)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnClear = QtGui.QPushButton(ParseChain)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.horizontalLayout.addWidget(self.btnClear)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(ParseChain)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.chkRootCerts = QtGui.QCheckBox(ParseChain)
        self.chkRootCerts.setObjectName(_fromUtf8("chkRootCerts"))
        self.horizontalLayout.addWidget(self.chkRootCerts)
        self.chkBody = QtGui.QCheckBox(ParseChain)
        self.chkBody.setObjectName(_fromUtf8("chkBody"))
        self.horizontalLayout.addWidget(self.chkBody)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnClose = QtGui.QPushButton(ParseChain)
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ParseChain)
        QtCore.QMetaObject.connectSlotsByName(ParseChain)

    def retranslateUi(self, ParseChain):
        ParseChain.setWindowTitle(_translate("ParseChain", "Parse CA Chain", None))
        self.label.setText(_translate("ParseChain", "Select CA chain file, then click <b>Parse</b> to see what new CAs will be appended to <b>QNetworkRequest\'s QSslConfiguration.caCertificates()</b>", None))
        self.btnChainSelect.setText(_translate("ParseChain", "...", None))
        self.btnParse.setText(_translate("ParseChain", "Parse", None))
        self.btnClear.setText(_translate("ParseChain", "Clear", None))
        self.label_2.setText(_translate("ParseChain", "Show", None))
        self.chkRootCerts.setText(_translate("ParseChain", "root certs", None))
        self.chkBody.setText(_translate("ParseChain", "cert body", None))
        self.btnClose.setText(_translate("ParseChain", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ParseChain = QtGui.QDialog()
    ui = Ui_ParseChain()
    ui.setupUi(ParseChain)
    ParseChain.show()
    sys.exit(app.exec_())

