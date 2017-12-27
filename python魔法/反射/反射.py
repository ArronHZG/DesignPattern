# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 反射.py
@time: 2017/12/22 0022 14:26
https://www.cnblogs.com/vipchenwei/p/6991209.html
https://www.cnblogs.com/Guido-admirers/p/6206212.html

'''
import commons


def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    if hasattr(commons, inp):
        func = getattr(commons, inp)
        func()
    else:
        print("404")


if __name__ == '__main__':
    run()