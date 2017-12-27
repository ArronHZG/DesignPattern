# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 策略模式.py
@time: 2017/12/19 0019 11:53

中文名 策略模式
外文名 Pattern:Strategy
抽象策略角色 由一个接口或者抽象类实现
具体策略角色 包装了相关的算法和行为 环境角色 持有一个策略类的引用

策略模式是指对一系列的算法定义，并将每一个算法封装起来，而且使它们还可以相互替换。策略模式让算法独立于使用它的客户而独立变化。
策略模式的优点有：策略模式提供了管理相关的算法族的办法、策略模式提供了可以替换继承关系的办法、使用策略模式可以避免使用多重条件转移语句。
'''
import abc


class Context():
    def __init__(self, strategy):
        self.__strategy = strategy

    def contextInterface(self):
        self.__strategy.AlgorithmInterface()


class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def AlgorithmInterface(self): pass


class ContextStrategyA(Strategy):
    def AlgorithmInterface(self):
        print('算法A')


# context = Context(ContextStrategyA())
# context.contextInterface()
# 结合工厂模型
class ContextFactory:
    algorithm={'算法A':Context(ContextStrategyA())}
    @classmethod
    def createContext(cls,str):
        return cls.algorithm[str]



algoA=ContextFactory.createContext('算法A')
algoA.contextInterface()