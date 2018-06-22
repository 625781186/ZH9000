# encoding=utf-8
import sys

# 程序主入口

# 首先你需要在引用的python文件内导入该对象所在的文件，也就是TestWindow.py
from PyQt4.QtCore import *
from MainWindow import Ui_MainWindow
from PyQt4.QtGui import *

from SampleInfoFunction import SampleInfoWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    # 这里的第一个变量是你该窗口的类型，第二个是该窗口对象。
    # 这里是主窗口类型。所以设置成当 QtGui.QMainWindow。
    # 你的窗口是一个会话框时你需要设置成: QtGui.QDialog
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def changeTemperature(self, temp):
        self.temperature.setText(temp)

    @pyqtSignature("")
    def openSampleInfoWindow(self):
        self.sampleInfoWindow = SampleInfoWindow()
        self.sampleInfoWindow.show()


