# encoding=utf-8
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import *
from SampleInfo import Ui_SampleInfoWindow
from MySQLConnection import *
from DetectItemIdDict import *
from datetime import *

class SampleInfoWindow(QWidget, Ui_SampleInfoWindow):
    waitingDetectList = []

    def __init__(self):
        QWidget.__init__(self)
        Ui_SampleInfoWindow.__init__(self)
        self.setupUi(self)

        # 禁止用户编辑
        self.QTableWidget_allItems.setEditTriggers(QTableWidget.NoEditTriggers)

        rst = MySQLConnextion.executeSQL("select `english_abbr` from `detect_item_info_table`")
        index = 0
        rows = self.QTableWidget_allItems.rowCount()
        for row in rst:
            self.QTableWidget_allItems.setItem(index / rows, index % rows, QTableWidgetItem(row[0]))
            index += 1

    @pyqtSignature("")
    def addItem(self, item = None):
        if item == None:
            return
        self.QTextBrowser_waitingDetect.moveCursor(QTextCursor.End)
        self.QTextBrowser_waitingDetect.insertPlainText(item.text() + '\t')
        self.waitingDetectList.append(item.text())

    @pyqtSignature("")
    def clearAllItems(self):
        self.waitingDetectList = []
        self.QTextBrowser_waitingDetect.clear()

    @pyqtSignature("")
    def test(self):
        try:
            rst = MySQLConnextion.executeSQL("SELECT `id` FROM `detect_item_info_table`")
        except Exception as e:
            print "数据库查询失败"

    @pyqtSignature("")
    def saveSampleMessage(self):
        sampleIndex = self.QLineEdit_sampleIndex.text()
        rackBarcode = self.QLineEdit_rackBarcode.text()
        holeIndex = self.QLineEdit_holeIndex.text()
        # item 的类型为 QString 并不是 python 中的 string,请务必进行类型转换（是个坑！务必小心）
        for item in self.waitingDetectList:
            sql = "INSERT INTO `detect_serial_info_table`(patient_id, rack_barcode, hole_index, detect_item_id, start_time) VALUES (%s, %s, %s, %s, %s)"
            try:
                MySQLConnextion.executeSQL(sql, (sampleIndex, rackBarcode, holeIndex, detectItemMap.get(str(item)), datetime.now()))
            except Exception as exp:
                print('输入值不能为空')
        pass