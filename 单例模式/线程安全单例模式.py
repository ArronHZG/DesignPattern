# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 线程安全单例模式.py
@time: 2017/12/24 0024 16:27
'''

import threading
import time

class Singleton():
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if (cls.__instance == None):
            Singleton.__lock.acquire()
            if (cls.__instance == None):
                cls.__instance = super().__new__(cls)
            # cls.__instance = super().__new__(cls)
            Singleton.__lock.release()
        return cls.__instance
    # def __new__(cls, *args, **kwargs):
    #     if (cls._instance == None):
    #         Singleton.__lock.acquire()
    #         # if (cls.__instance == None):
    #         cls._instance = super().__new__(cls)
    #         # Singleton.__lock.release()
    #     return cls._instance

class A(Singleton):
    def __init__(self,s):
        self.s=s
        # time.sleep()

def threadfun(s):
    for i in s:
        a = A(i)
        print(id(a), a.s)

if __name__=='__main__':
    # print(A._instance)
    # a=A('apple')
    # print(id(a), a.s)
    # b=A('banana')
    # print(id(a),a.s)
    # print(id(b),b.s)
    # print(super(a.__class__))
    # print(a.__class__.mro())
    # print(A._instance)
    threading.Thread(target=threadfun, args=('aaaaaa',)).start()   # 创建一个线程ta，执行 threadfun()
    threading.Thread(target=threadfun, args=('bbbbbbbb',)).start()  # 创建一个线程tb，执行threadfun()
    threading.Thread(target=threadfun, args=('cccccccc',)).start()  # 创建一个线程ta，执行 threadfun()
    threading.Thread(target=threadfun, args=('ddddd',)).start() # 创建一个线程tb，执行threadfun()
    threading.Thread(target=threadfun, args=('aaaaaa',)).start()  # 创建一个线程ta，执行 threadfun()
    threading.Thread(target=threadfun, args=('bbbbbbbb',)).start()  # 创建一个线程tb，执行threadfun()
    threading.Thread(target=threadfun, args=('cccccccc',)).start()  # 创建一个线程ta，执行 threadfun()
    threading.Thread(target=threadfun, args=('ddddd',)).start()  # 创建一个线程tb，执行threadfun()
    threading.Thread(target=threadfun, args=('aaaaaa',)).start()  # 创建一个线程ta，执行 threadfun()
    threading.Thread(target=threadfun, args=('bbbbbbbb',)).start()  # 创建一个线程tb，执行threadfun()
    threading.Thread(target=threadfun, args=('cccccccc',)).start()  # 创建一个线程ta，执行 threadfun()
    threading.Thread(target=threadfun, args=('ddddd',)).start()  # 创建一个线程tb，执行threadfun()
    threading.Thread(target=threadfun, args=('aaaaaa',)).start()  # 创建一个线程ta，执行 threadfun()
    threading.Thread(target=threadfun, args=('bbbbbbbb',)).start()  # 创建一个线程tb，执行threadfun()
    threading.Thread(target=threadfun, args=('cccccccc',)).start()  # 创建一个线程ta，执行 threadfun()
    threading.Thread(target=threadfun, args=('ddddd',)).start()  # 创建一个线程tb，执行threadfun()
    # ta.start()  # 调用start()，运行线程
    # tb.start()  # 调用start()，运行线程
    # ta.start()  # 调用start()，运行线程
    # tb.start()  # 调用start()，运行线程
