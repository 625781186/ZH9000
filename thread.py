# coding: utf-8

import Queue
import random
import threading
import time
import sys

que = Queue.Queue()

# 生产者
def producer():
    global que
    while True:
        i = random.randint(0, 10)
        que.put(i)
        print "%s: %d to the queue is produced !\n" % ("生产者", i)
        time.sleep(0.5)

# 消费者
def consumer():
    global que
    while True:
        val = que.get()
        print "%s: %d in the queue is consumed!\n" % ("消费者", val)
        time.sleep(0.5)

# 主线程
if __name__ == '__main__':
    for i in range(1):
        p = threading.Thread(target=producer)
        p.start()
    for i in range(1):
        c = threading.Thread(target=consumer)
        c.start()