# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 工厂方法模式.py
@time: 2017/12/21 0021 8:01
中文名
工厂方法模式
外文名 Factory Method
角    色 抽象与具体工厂，抽象与具体产品
应    用 软件设计
中文名 工厂方法模式 外文名 Factory Method 角    色 抽象与具体工厂，抽象与具体产品 应    用 软件设计


抽象工厂(Creator)角色：是工厂方法模式的核心，与应用程序无关。任何在模式中创建的对象的工厂类必须实现这个接口。
具体工厂(Concrete Creator)角色：这是实现抽象工厂接口的具体工厂类，包含与应用程序密切相关的逻辑，并且受到应用程序调用以创建产品对象。在上图中有两个这样的角色：BulbCreator与TubeCreator。
抽象产品(Product)角色：工厂方法模式所创建的对象的超类型，也就是产品对象的共同父类或共同拥有的接口。在上图中，这个角色是Light。
具体产品(Concrete Product)角色：这个角色实现了抽象产品角色所定义的接口。某具体产品有专门的具体工厂创建，它们之间往往一一对应。
模式应用编辑
工厂方法经常用在以下两种情况中:
第一种情况是对于某个产品，调用者清楚地知道应该使用哪个具体工厂服务，实例化该具体工厂，生产出具体的产品来。Java Collection中的iterator() 方法即属于这种情况。
第二种情况，只是需要一种产品，而不想知道也不需要知道究竟是哪个工厂为生产的，即最终选用哪个具体工厂的决定权在生产者一方，它们根据当前系统的情况来实例化一个具体的工厂返回给使用者，而这个决策过程这对于使用者来说是透明的。
'''

# 修改简单工厂模式
from 简单工厂模式 import OperationAdd, OperationSub, OperationMul, OperationDiv,OperationPower
from abc import abstractmethod, ABCMeta


class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def createOperation(self): pass


class AddFactory(IFactory):
    def createOperation(self):
        return OperationAdd()

class SubFactory(IFactory):
    def createOperation(self):
        return OperationSub()

class MulFactory(IFactory):
    def createOperation(self):
        return OperationMul()

class DivFactory(IFactory):
    def createOperation(self):
        return OperationDiv()


class PowerFactory(IFactory):
    def createOperation(self):
        return OperationPower()
...
if __name__=="__main__":
    oper = AddFactory().createOperation()
    oper.setNumberA(5)
    oper.setNumberB(2)
    print(oper.getResult())
