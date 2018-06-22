# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 768)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.temperature = QtGui.QLabel(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(150, 30, 111, 31))
        self.temperature.setStyleSheet(_fromUtf8(""))
        self.temperature.setFrameShape(QtGui.QFrame.Box)
        self.temperature.setText(_fromUtf8(""))
        self.temperature.setObjectName(_fromUtf8("temperature"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 108, 24))
        self.label.setObjectName(_fromUtf8("label"))
        self.addSampleMessage = QtGui.QPushButton(self.centralwidget)
        self.addSampleMessage.setGeometry(QtCore.QRect(780, 600, 150, 46))
        self.addSampleMessage.setObjectName(_fromUtf8("addSampleMessage"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 37))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.addSampleMessage, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.openSampleInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "温度：", None))
        self.addSampleMessage.setText(_translate("MainWindow", "添加样本信息", None))

