# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 多线程.py
@time: 2017/12/24 0024 16:40
'''
import threading


def threadfun(x, y, z=1):  # 线程任务函数 threadfun()
    for i in range(x, y, z):
        print(i)


ta = threading.Thread(target=threadfun, args=(60, 100, 2))  # 创建一个线程ta，执行 threadfun()
tb = threading.Thread(target=threadfun, args=(10, 50))  # 创建一个线程tb，执行threadfun()
ta.start()  # 调用start()，运行线程
tb.start()  # 调用start()，运行线程
'''''打印：1 2 3 4 5 10 11 12 13 14'''
