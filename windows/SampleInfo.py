# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SampleInfo.ui'
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

class Ui_SampleInfoWindow(object):
    def setupUi(self, SampleInfoWindow):
        SampleInfoWindow.setObjectName(_fromUtf8("SampleInfoWindow"))
        SampleInfoWindow.resize(728, 575)
        self.QLineEdit_sampleBarcode = QtGui.QLineEdit(SampleInfoWindow)
        self.QLineEdit_sampleBarcode.setGeometry(QtCore.QRect(106, 51, 153, 20))
        self.QLineEdit_sampleBarcode.setObjectName(_fromUtf8("QLineEdit_sampleBarcode"))
        self.label_3 = QtGui.QLabel(SampleInfoWindow)
        self.label_3.setGeometry(QtCore.QRect(504, 24, 42, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(SampleInfoWindow)
        self.label.setGeometry(QtCore.QRect(43, 24, 42, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(SampleInfoWindow)
        self.label_2.setGeometry(QtCore.QRect(267, 24, 70, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(SampleInfoWindow)
        self.label_4.setGeometry(QtCore.QRect(43, 51, 56, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.QLineEdit_sampleIndex = QtGui.QLineEdit(SampleInfoWindow)
        self.QLineEdit_sampleIndex.setGeometry(QtCore.QRect(106, 24, 153, 20))
        self.QLineEdit_sampleIndex.setObjectName(_fromUtf8("QLineEdit_sampleIndex"))
        self.QLineEdit_holeIndex = QtGui.QLineEdit(SampleInfoWindow)
        self.QLineEdit_holeIndex.setGeometry(QtCore.QRect(553, 24, 153, 20))
        self.QLineEdit_holeIndex.setObjectName(_fromUtf8("QLineEdit_holeIndex"))
        self.QLineEdit_rackBarcode = QtGui.QLineEdit(SampleInfoWindow)
        self.QLineEdit_rackBarcode.setGeometry(QtCore.QRect(344, 24, 153, 20))
        self.QLineEdit_rackBarcode.setObjectName(_fromUtf8("QLineEdit_rackBarcode"))
        self.Btn_test = QtGui.QPushButton(SampleInfoWindow)
        self.Btn_test.setGeometry(QtCore.QRect(43, 332, 88, 27))
        self.Btn_test.setObjectName(_fromUtf8("Btn_test"))
        self.Btn_clear = QtGui.QPushButton(SampleInfoWindow)
        self.Btn_clear.setGeometry(QtCore.QRect(306, 298, 88, 27))
        self.Btn_clear.setObjectName(_fromUtf8("Btn_clear"))
        self.QTextBrowser_waitingDetect = QtGui.QTextBrowser(SampleInfoWindow)
        self.QTextBrowser_waitingDetect.setGeometry(QtCore.QRect(43, 99, 256, 192))
        self.QTextBrowser_waitingDetect.setObjectName(_fromUtf8("QTextBrowser_waitingDetect"))
        self.label_5 = QtGui.QLabel(SampleInfoWindow)
        self.label_5.setGeometry(QtCore.QRect(43, 78, 84, 16))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Btn_save = QtGui.QPushButton(SampleInfoWindow)
        self.Btn_save.setGeometry(QtCore.QRect(306, 332, 88, 27))
        self.Btn_save.setObjectName(_fromUtf8("Btn_save"))
        self.QTableWidget_allItems = QtGui.QTableWidget(SampleInfoWindow)
        self.QTableWidget_allItems.setGeometry(QtCore.QRect(306, 366, 256, 192))
        self.QTableWidget_allItems.setShowGrid(False)
        self.QTableWidget_allItems.setRowCount(5)
        self.QTableWidget_allItems.setColumnCount(7)
        self.QTableWidget_allItems.setObjectName(_fromUtf8("QTableWidget_allItems"))
        self.QTableWidget_allItems.horizontalHeader().setVisible(False)
        self.QTableWidget_allItems.verticalHeader().setVisible(False)
        self.QLineEdit_test = QtGui.QLineEdit(SampleInfoWindow)
        self.QLineEdit_test.setGeometry(QtCore.QRect(43, 301, 153, 20))
        self.QLineEdit_test.setObjectName(_fromUtf8("QLineEdit_test"))

        self.retranslateUi(SampleInfoWindow)
        QtCore.QObject.connect(self.Btn_test, QtCore.SIGNAL(_fromUtf8("clicked()")), SampleInfoWindow.test)
        QtCore.QObject.connect(self.Btn_save, QtCore.SIGNAL(_fromUtf8("clicked()")), SampleInfoWindow.saveSampleMessage)
        QtCore.QObject.connect(self.QTableWidget_allItems, QtCore.SIGNAL(_fromUtf8("itemClicked(QTableWidgetItem*)")), SampleInfoWindow.addItem)
        QtCore.QObject.connect(self.Btn_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), SampleInfoWindow.clearAllItems)
        QtCore.QMetaObject.connectSlotsByName(SampleInfoWindow)

    def retranslateUi(self, SampleInfoWindow):
        SampleInfoWindow.setWindowTitle(_translate("SampleInfoWindow", "SampleInfoWindow", None))
        self.label_3.setText(_translate("SampleInfoWindow", "孔位号", None))
        self.label.setText(_translate("SampleInfoWindow", "样本号", None))
        self.label_2.setText(_translate("SampleInfoWindow", "试管架条码", None))
        self.label_4.setText(_translate("SampleInfoWindow", "样本条码", None))
        self.Btn_test.setText(_translate("SampleInfoWindow", "Test", None))
        self.Btn_clear.setText(_translate("SampleInfoWindow", "重置", None))
        self.label_5.setText(_translate("SampleInfoWindow", "病人检测项目", None))
        self.Btn_save.setText(_translate("SampleInfoWindow", "确认", None))

