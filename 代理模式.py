# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 代理模式.py
@time: 2017/12/21 0021 7:46

中文名 代理模式 外文名 Proxy Pattern
组    成 抽象角色、代理角色、真实角色
优    点 职责清晰
组成：
抽象角色：通过接口或抽象类声明真实角色实现的业务方法。
代理角色：实现抽象角色，是真实角色的代理，通过真实角色的业务逻辑方法来实现抽象方法，并可以附加自己的操作。
真实角色：实现抽象角色，定义真实角色所要实现的业务逻辑，供代理角色调用。

优点编辑
(1).职责清晰
真实的角色就是实现实际的业务逻辑，不用关心其他非本职责的事务，通过后期的代理完成一件完成事务，附带的结果就是编程简洁清晰。
(2).代理对象可以在客户端和目标对象之间起到中介的作用，这样起到了中介的作用和保护了目标对象的作用。
(3).高扩展性

'''
import abc


class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def request(self): pass


class RealSubject(Subject):
    def request(self):
        return "真实对象"


class Proxy(Subject):
    def __init__(self):
        self.realSubject = RealSubject()
        print(self.realSubject.request())

    def request(self):
        return "代理对象"

print(Proxy().request())