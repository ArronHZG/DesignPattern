# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 依赖注入.py
@time: 2017/12/19 0019 12:50
'''


# =================================依赖注入案例一======================================
# metaclass是类的模板，所以必须从`type`类型派生：元类
class MyType(type):
    def __call__(cls, *args, **kwargs):  ##执行Type的__call__方法，这里的cls就是<__main__.Foo object at 0x001B59F0> Foo类
        obj = cls.__new__(cls, *args, **kwargs)  ##Foo的__new__方法
        if cls == Foo1:
            obj.__init__(Foo())
        elif cls == Foo2:
            obj.__init__(Foo1())
        return obj


class Foo(metaclass=MyType):
    def __init__(self, args):
        print('======Foo======')
        self.name = args

    def f(self):
        print(self.name)


class Foo1(metaclass=MyType):
    def __init__(self, args):
        print('======Foo1======')
        self.name = args
        print(self.name)

    def f1(self):
        print(self.name)


class Foo2(metaclass=MyType):
    def __init__(self, args):
        print('======Foo2======')
        self.name = args

    def f2(self):
        print(self.name)


obj = Foo2(123)
obj.f2()














