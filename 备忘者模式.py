# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 备忘者模式.py
@time: 2017/12/23 0023 15:57
备忘录模式（Memento Pattern）保存一个对象的某个状态，以便在适当的时候恢复对象。备忘录模式属于行为型模式。
介绍
意图：在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。
主要解决：所谓备忘录模式就是在不破坏封装的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态，这样可以在以后将对象恢复到原先保存的状态。
何时使用：很多时候我们总是需要记录一个对象的内部状态，这样做的目的就是为了允许用户取消不确定或者错误的操作，能够恢复到他原先的状态，使得他有"后悔药"可吃。
如何解决：通过一个备忘录类专门存储对象状态。
关键代码：客户不与备忘录类耦合，与备忘录管理类耦合。
应用实例： 1、后悔药。 2、打游戏时的存档。 3、Windows 里的 ctri + z。 4、IE 中的后退。 4、数据库的事务管理。
优点： 1、给用户提供了一种可以恢复状态的机制，可以使用户能够比较方便地回到某个历史的状态。 2、实现了信息的封装，使得用户不需要关心状态的保存细节。
缺点：消耗资源。如果类的成员变量过多，势必会占用比较大的资源，而且每一次保存都会消耗一定的内存。
使用场景： 1、需要保存/恢复数据的相关状态场景。 2、提供一个可回滚的操作。
注意事项： 1、为了符合迪米特原则，还要增加一个管理备忘录的类。 2、为了节约内存，可使用原型模式+备忘录模式。
'''


class Parameter:
    # a=1
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None  # 需要保存的参数
        self.d = None


class Originator(Parameter):  # 使用宽接口,可以访问备忘录中的内容
    def __init__(self):
        super().__init__()

    def createMemento(self):  # 创建备忘录
        mome = Memento(**self.__dict__)
        return mome

    def setMemento(self, mome):  # 恢复备忘录
        self.__dict__.update(mome.__dict__)

        # def __init__(self, id, **kw):
        #     Pototype.__init__(self,id,**kw)


class Memento(Parameter):
    # def __init__(self):
    #     Parameter.__init__(self)
    def __init__(self, **kw):
        super().__init__()
        self.__dict__.update(kw)


class Caretaker:  # 使用窄接口,只能传递Momento
    # def __init__(self):
    #     self.__meme=Memento()
    def setMemento(self, meme):
        self.__meme = meme

    def getMemento(self):
        return self.__meme


if __name__ == '__main__':
    originator = Originator()
    caretaker = Caretaker()
    # print(caretaker.getMemento().__dict__)
    originator.a = 1
    originator.b = 2
    originator.c = 3
    originator.d = 4
    caretaker.setMemento(originator.createMemento())
    print(caretaker.getMemento().__dict__)

    originator.a = 1
    originator.b = 1
    originator.c = 1
    originator.d = 1
    # meme1 = originator.createMemento()
    print(originator.__dict__)
    originator.setMemento(caretaker.getMemento())
    print(originator.__dict__)
