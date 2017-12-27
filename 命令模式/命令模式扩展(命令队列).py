# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 命令模式扩展(命令队列).py
@time: 2017/12/24 0024 18:02

http://www.cnblogs.com/JsonShare/p/7206395.html

'''

# from abc import ABCMeta, abstractmethod
from 命令模式 import Command


# class Command(metaclass=ABCMeta):
#     def __init__(self, receiver):
#         self.receiver = receiver
#
#     @abstractmethod
#     def execute(self): pass


class TVOnCommand(Command):
    def __init(self, receiver):
        super.__init__(receiver)

    def execute(self):
        self.receiver.on()


class TVOffCommand(Command):
    def __init(self, receiver):
        super.__init__(receiver)

    def execute(self):
        self.receiver.off()


class Invoker:
    '''
    请求者角色类  -- 遥控器Invoker
    '''

    def __init__(self):
        self.commands = []

    def setCommand(self, command):
        self.commands.append(command)

    def executeCommands(self):
        for c in self.commands:
            c.execute()
            # self.commands.pop(0)
        self.commands = []


class TV:
    '''
    class Receiver 命令的接受者,具体命令操纵的对象
    '''

    def __init__(self):
        self.on_state = '开机'
        self.off_state = '关机'
        self.state = self.off_state


    def on(self):
        if self.state == self.off_state:
            self.state = self.on_state
            print(self.state)
        else:
            print('电视已' + self.on_state)

    def off(self):
        if self.state == self.on_state:
            self.state = self.off_state
            print(self.state)
        else:
            print('电视已' + self.off_state)


if __name__ == '__main__':
    tv = TV()
    # 创建客户端,发出命令
    tvOn = TVOnCommand(tv)
    tvOff = TVOffCommand(tv)

    # 真正的执行客户端,执行命令
    i = Invoker()
    i.setCommand(tvOn)
    i.setCommand(tvOn)
    i.setCommand(tvOff)

    # TV.on_state = '关机'
    # print(TV.__dict__)
    i.setCommand(tvOn)
    i.setCommand(tvOff)
    i.setCommand(tvOn)
    i.setCommand(tvOff)
    i.executeCommands()
