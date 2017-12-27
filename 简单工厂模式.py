# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 简单工厂模式.py
@time: 2017/12/18 0018 6:26
中文名 简单工厂模式
外文名 Factory Method Pattern
属    于 创建型模式
别    称 静态工厂方法

简单工厂模式是属于创建型模式，又叫做静态工厂方法（Static Factory Method）模式，但不属于23种GOF设计模式之一。简单工厂模式是由一个工厂对象决定创建出哪一种产品类的实例。简单工厂模式是工厂模式家族中最简单实用的模式，可以理解为是不同工厂模式的一个特殊实现。


'''
import abc


class Operation(metaclass=abc.ABCMeta):

    def setNumberA(self, number):
        self.__numberA = number

    def getNumberA(self):
        return self.__numberA

    def setNumberB(self, number):
        self.__numberB = number

    def getNumberB(self):
        return self.__numberB

    @abc.abstractmethod
    def getResult(self): pass


class OperationAdd(Operation):

    def getResult(self):
        self.__result = Operation.getNumberA(self) + Operation.getNumberB(self)
        return self.__result


class OperationSub(Operation):
    def getResult(self):
        self.__result = Operation.getNumberA(self) - Operation.getNumberB(self)
        return self.__result


class OperationMul(Operation):
    def getResult(self):
        self.__result = Operation.getNumberA(self) * Operation.getNumberB(self)
        return self.__result


class OperationDiv(Operation):
    def getResult(self):
        try:
            self.__result = Operation.getNumberA(self) / Operation.getNumberB(self)
        except ZeroDivisionError as e:
            print('ZeroDivisionError')
        return self.__result

    pass


class OperationPower(Operation):
    def getResult(self):
        self.__result = Operation.getNumberA(self) ** Operation.getNumberB(self)
        return self.__result


class OperationFactory:
    switcher = {'+': OperationAdd(), '-': OperationSub(), '*': OperationMul(), '/': OperationDiv()}

    @classmethod
    def createOperate(cls, operate):

        try:
            return cls.switcher[operate]
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    oper = OperationFactory.createOperate('/')
    try:
        oper.setNumberA(5)
        oper.setNumberB(2)
    except AttributeError as e:
        print('AttributeError')
    except BaseException as e:
        print(e)
    try:
        print(oper.getResult())
    except:
        pass
