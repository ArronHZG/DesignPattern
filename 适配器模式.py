# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 适配器模式.py
@time: 2017/12/23 0023 15:43
'''
from abc import ABCMeta, abstractmethod


class Client():
    def act(self):
        tar = Adepter()
        tar.t_act()


class Target(metaclass=ABCMeta):
    @abstractmethod
    def t_act(self): pass


class Adepter(Target):
    def t_act(self):
        adeptee = Adeptee()
        adeptee.A_act()


class Adeptee():
    def A_act(self):
        print('适配者行为')


if __name__ == '__main__':
    c = Client()
    c.act()
