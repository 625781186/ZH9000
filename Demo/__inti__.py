# encoding=utf-8
import sys
import threading

from windows.MainWindowFunction import MainWindow
from windows.MainWindow import *
from ComMessage import ComMessage
from MySQLConnection import *

import time
import Queue
import serial

# 初始化发送信息队列
sendQueue = Queue.Queue()
# 初始化接受信息队列
receiveQueue = Queue.Queue()
# 初始化串口
ser = serial.Serial('COM2', 115200, timeout=0.1)

# 从发送队列中取出信息，进行打包后发送
def sendQueueConsumer():
    global sendQueue
    global ser
    while True:
        message = ComMessage.package(sendQueue.get())
        # 调用串口发送信息
        ser.write(message)
        print message
        time.sleep(0.03)

# 从接收队列中取出信息，进行解包后处理
def recvQueueConsumer():
    global receiveQueue
    while True:
        message = ComMessage.unpackage(receiveQueue.get())
        print(message)
        # 依据 message 进行处理
        # 通过字典来实现 Switch case

        time.sleep(0.03)

# 从串口中读取数据，将其存储在接收消息队列中
def recvQueueProducer():
    global receiveQueue
    global ser
    while True:
        message = ser.readline()
        if message != '':
            # message = bytes(message)
            receiveQueue.put(message)
        time.sleep(0.03)

def sendSampleMessage(rackBarcode, holeIndex):
    global sendQueue
    sql = "SELECT `detect_item_id` FROM `detect_serial_info_table` WHERE `rack_barcode` = %s AND `hole_index` = %s AND `detect_state` = 0"
    rst = MySQLConnextion.executeSQL(sql, (rackBarcode, holeIndex))
    message = ['\x01', '\x00', '\x00', '\x00', '\x01']
    for row in rst:
        message.append(chr(row[0]))
        message.append('*')
    print message
    sendQueue.put(message)

def init():
    sendThread = threading.Thread(target=sendQueueConsumer)
    recvConsumeThread = threading.Thread(target=recvQueueConsumer)
    recvProduceThread = threading.Thread(target=recvQueueProducer)

    sendThread.start()
    recvConsumeThread.start()
    recvProduceThread.start()

    data = ['\x01', '\x00', '\x00', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23',
            '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23',
            '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23', '\x23']
    # data = ['\x01', '\x00', '\x00', '\x23', '\x23', '\x23']
    # data = ['\x01', '\x00', '\x00', '\x31', '\x32', '\x23']
    global sendQueue
    # sendQueue.put(data)
    sendSampleMessage(123, 1)


if __name__ == "__main__":
    init()
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()  # 创建Qt对象
    mainWindow.show()  # Qt对象显示
    sys.exit(app.exec_())



