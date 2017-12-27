# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 装饰模式.py
@time: 2017/12/19 0019 14:14

中文名 装饰模式
外文名 Decorator Pattern
类    别 DesignPattern 又    名 装饰者模式
设计原则  多用组合，少用继承

以下情况使用Decorator模式
1. 需要扩展一个类的功能，或给一个类添加附加职责。
2. 需要动态的给一个对象添加功能，这些功能可以再动态的撤销。
3. 需要增加由一些基本功能的排列组合而产生的非常大量的功能，从而使继承关系变的不现实。
4. 当不能采用生成子类的方法进行扩充时。一种情况是，可能有大量独立的扩展，为支持每一种组合将产生大量的子类，使得子类数目呈爆炸性增长。另一种情况可能是因为类定义被隐藏，或类定义不能用于生成子类。
1. Decorator模式与继承关系的目的都是要扩展对象的功能，但是Decorator可以提供比继承更多的灵活性。
优点
2. 通过使用不同的具体装饰类以及这些装饰类的排列组合，设计师可以创造出很多不同行为的组合。


在装饰模式中的各个角色有：
　　（1）抽象构件（Component）角色：给出一个抽象接口，以规范准备接收附加责任的对象。
　　（2）具体构件（Concrete Component）角色：定义一个将要接收附加责任的类。
　　（3）装饰（Decorator）角色：持有一个构件（Component）对象的实例，并实现一个与抽象构件接口一致的接口。
　　（4）具体装饰（Concrete Decorator）角色：负责给构件对象添加上附加的责任。

'''
import abc


class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self): pass


class ConcreteComponentA(Component):
    def operation(self):
        return "小明"


class ConcreteComponentB(Component):
    def operation(self):
        return "花花"


class Decorator(Component):
    def setComponent(self, component):
        self.component = component

    def operation(self): pass


class ConcreteDecoratorA(Decorator):
    def __init__(self):
        self.decorator = "戴帽子"

    def operation(self):
        return self.component.operation() + self.decorator


class ConcreteDecoratorB(Decorator):
    def behavior(self):
        return self.component.operation() + "在洗澡"

    def operation(self):
        return self.behavior()



decoB = ConcreteDecoratorB()#洗澡
decoB.setComponent(ConcreteComponentA())
print(decoB.operation())


decoA = ConcreteDecoratorA()#戴帽子
decoA.setComponent(ConcreteComponentA())
print(decoA.operation())
decoA.setComponent(decoB)
print(decoA.operation())

