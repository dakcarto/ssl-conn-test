# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/testbrowser.ui'
#
# Created: Tue Mar  3 18:06:07 2015
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

class Ui_TestBrowser(object):
    def setupUi(self, TestBrowser):
        TestBrowser.setObjectName(_fromUtf8("TestBrowser"))
        TestBrowser.resize(900, 720)
        self.verticalLayout = QtGui.QVBoxLayout(TestBrowser)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.backButton = QtGui.QToolButton(TestBrowser)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout.addWidget(self.backButton)
        self.forwardButton = QtGui.QToolButton(TestBrowser)
        self.forwardButton.setObjectName(_fromUtf8("forwardButton"))
        self.horizontalLayout.addWidget(self.forwardButton)
        self.reloadButton = QtGui.QToolButton(TestBrowser)
        self.reloadButton.setObjectName(_fromUtf8("reloadButton"))
        self.horizontalLayout.addWidget(self.reloadButton)
        self.stopButton = QtGui.QToolButton(TestBrowser)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.comboBox = QtGui.QComboBox(TestBrowser)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox.setEditable(True)
        self.comboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox.setMinimumContentsLength(200)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.goButton = QtGui.QToolButton(TestBrowser)
        self.goButton.setObjectName(_fromUtf8("goButton"))
        self.horizontalLayout.addWidget(self.goButton)
        self.line = QtGui.QFrame(TestBrowser)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.sourceButton = QtGui.QToolButton(TestBrowser)
        self.sourceButton.setObjectName(_fromUtf8("sourceButton"))
        self.horizontalLayout.addWidget(self.sourceButton)
        self.pageResetButton = QtGui.QToolButton(TestBrowser)
        self.pageResetButton.setObjectName(_fromUtf8("pageResetButton"))
        self.horizontalLayout.addWidget(self.pageResetButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.vertSplitter = QtGui.QSplitter(TestBrowser)
        self.vertSplitter.setOrientation(QtCore.Qt.Vertical)
        self.vertSplitter.setChildrenCollapsible(False)
        self.vertSplitter.setObjectName(_fromUtf8("vertSplitter"))
        self.webView = QtWebKit.QWebView(self.vertSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.vertSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.vertSplitter)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.clearButton = QtGui.QToolButton(TestBrowser)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout_2.addWidget(self.clearButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(TestBrowser)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.cmbxProtocol = QtGui.QComboBox(TestBrowser)
        self.cmbxProtocol.setObjectName(_fromUtf8("cmbxProtocol"))
        self.horizontalLayout_4.addWidget(self.cmbxProtocol)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnAuthSelect = QtGui.QToolButton(TestBrowser)
        self.btnAuthSelect.setObjectName(_fromUtf8("btnAuthSelect"))
        self.horizontalLayout_3.addWidget(self.btnAuthSelect)
        self.leAuthId = QtGui.QLineEdit(TestBrowser)
        self.leAuthId.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leAuthId.setObjectName(_fromUtf8("leAuthId"))
        self.horizontalLayout_3.addWidget(self.leAuthId)
        self.clearAuthButton = QtGui.QToolButton(TestBrowser)
        self.clearAuthButton.setMaximumSize(QtCore.QSize(20, 20))
        self.clearAuthButton.setObjectName(_fromUtf8("clearAuthButton"))
        self.horizontalLayout_3.addWidget(self.clearAuthButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.btnAuthEditor = QtGui.QToolButton(TestBrowser)
        self.btnAuthEditor.setObjectName(_fromUtf8("btnAuthEditor"))
        self.horizontalLayout_2.addWidget(self.btnAuthEditor)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(TestBrowser)
        QtCore.QMetaObject.connectSlotsByName(TestBrowser)

    def retranslateUi(self, TestBrowser):
        TestBrowser.setWindowTitle(_translate("TestBrowser", "Dialog", None))
        self.backButton.setText(_translate("TestBrowser", "<", None))
        self.forwardButton.setText(_translate("TestBrowser", ">", None))
        self.reloadButton.setText(_translate("TestBrowser", "Reload", None))
        self.stopButton.setText(_translate("TestBrowser", "Stop", None))
        self.goButton.setText(_translate("TestBrowser", "Go", None))
        self.sourceButton.setText(_translate("TestBrowser", "Source", None))
        self.pageResetButton.setText(_translate("TestBrowser", "Reset", None))
        self.clearButton.setText(_translate("TestBrowser", "Clear log", None))
        self.label.setText(_translate("TestBrowser", "SSL Protocol", None))
        self.btnAuthSelect.setText(_translate("TestBrowser", "Auth select...", None))
        self.clearAuthButton.setText(_translate("TestBrowser", "X", None))
        self.btnAuthEditor.setText(_translate("TestBrowser", "Auth editor...", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TestBrowser = QtGui.QDialog()
    ui = Ui_TestBrowser()
    ui.setupUi(TestBrowser)
    TestBrowser.show()
    sys.exit(app.exec_())

