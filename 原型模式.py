# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 原型模式.py
@time: 2017/12/21 0021 8:26

中文名 原型模式
外文名 Prototype
问    题 结构复杂的对象”的创建工作
实    现clone()方法来实现对象的克隆
模    式Prototype
'''
from abc import abstractmethod, ABCMeta
from copy import copy,deepcopy


class Pototype(metaclass=ABCMeta):
    def __init__(self, id, **kw):
        self.__id = id
        self.__dict__.update(kw)

    def getID(self):
        return self.__id

    def setID(self,id):
        self.__id = id

    @abstractmethod
    def clone(self): pass


class Client:
    pass


class ConcretePrototype1(Pototype):
    def __init__(self, id, **kw):
        Pototype.__init__(self,id,**kw)

    def clone(self):
        return copy(self)


class ConcretePrototype2(Pototype):
    def __init__(self, id, **kw):
        Pototype.__init__(self,id,**kw)

    def clone(self):
        return copy(self)

    def deepClone(self):
        return deepcopy(self)


class Point:
    __slots__ = ("x", "y")#限定动态绑定的参数
    def __init__(self, x, y):
        self.x = x
        self.y = y

id1=ConcretePrototype1(1,name='job')
id2=ConcretePrototype2(2,add='beijing',cla=id1)
copyid2=id2.clone()
print(copyid2.__dict__)
print(copyid2.__dict__['cla'].getID())
id1.setID(11)
print(copyid2.__dict__)
print(copyid2.__dict__['cla'].getID())
copyid2=id2.deepClone()
id1.setID(20)
print(copyid2.__dict__)
print(copyid2.__dict__['cla'].getID())
