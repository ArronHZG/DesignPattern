# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 命令模式扩展(宏命令).py
@time: 2017/12/24 0024 18:02


什么是宏命令呢？简单点说就是包含多个命令的命令，是一个命令的组合；

宏命令又称为组合命令，它是命令模式和组合模式联用的产物；

宏命令也是一个具体命令，不过它包含了对其他命令对象的引用，在调用宏命令的execute(self):方法时，将递归调用它所包含的每个成员命令的execute(self):方法，一个宏命令的成员对象可以是简单命令，还可以继续是宏命令。执行一个宏命令将执行多个具体命令，从而实现对命令的批处理。

我们可以定义“命令的命令”来实现（这种特殊的命令的execute方法内部是顺序调用其它若干命令的execute方法）
这里模拟一下电脑开机,按下开机键后，主要经历四个阶段：

BIOS -> 主引导记录（查询那个分区是操作系统）-> 硬盘启动 -> 操作系统

这里简化成四个命令：BIOSStartCommand、MBRStartCommand、HDDStartCommand、OSStartCommand；

具体实例代码：
'''
from 命令模式 import Command
from 组合模式 import Component

# class MacroCommand(Command):
#     '''
#     宏命令,扩充命令类
#     '''
#
#     @abstractmethod
#     def add(self, command): pass
#
#     @abstractmethod
#     def removeCommand(self, command): pass


# class ComputerMacroInvoker():
#     '''
#      宏命令接口实现
#     '''
#     def __init__(self):
#         self.commands = []
#
#     def execute(self):
#         for c in self.commands:
#             c.execute()
#         self.commands = []
#
#     def add(self, command):
#         self.commands.append((command))
#
#     def removeCommand(self, command):
#         self.commands.remove(command)


class Computer:
    def startBIOS(self):
        print("BIOS启动...")

    def startMBR(self):
        print("MBR加载...")

    def startHDD(self):
        print("HDD加载...")

    def startOS(self):
        print("系统启动...")

class BIOSStartCommand(Command):
    '''
    具体命令 - - BIOS启动命令
    '''
    def __init__(self,computer):
        self.__computer=computer

    def execute(self):
        self.__computer.startBIOS()


class MBRStartCommand(Command):
    '''
    具体命令 - - BIOS启动命令
    '''
    def __init__(self,computer):
        self.__computer=computer

    def execute(self):
        self.__computer.startMBR()

class HDDStartCommand(Command):
    '''
    具体命令 - - BIOS启动命令
    '''
    def __init__(self,computer):
        self.__computer=computer

    def execute(self):
        self.__computer.startHDD()

class OSStartCommand(Command):
    '''
    具体命令 - - BIOS启动命令
    '''
    def __init__(self,computer):
        self.__computer=computer

    def execute(self):
        self.__computer.startOS()


class ComputerMacroInvoker(Component):
    def __init__(self, command):
        super().__init__(command)
        self.command=command
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        if component in self.children:
            self.children.remove()
        else:
            print("没有该子成员")
            return False

    def executeChildren(self,depth):
        for c in self.children:
            c.display(depth)

    def executeSelf(self):
        self.command.execute()


    def display(self, depth):
        print('-' * depth,end='')
        self.executeSelf()
        self.executeChildren(depth+1)

if __name__ == '__main__':
    #调用客户端
    computer=Computer()
    biosCommand=BIOSStartCommand(computer)
    mbrCommand=MBRStartCommand(computer)
    hddCommand=HDDStartCommand(computer)
    osCommand=OSStartCommand(computer)


    #执行客户端
    invoker=ComputerMacroInvoker(biosCommand)
    # invoker.add(ComputerMacroInvoker(biosCommand))
    invoker.add(ComputerMacroInvoker(mbrCommand))
    invoker.children[0].add(ComputerMacroInvoker(hddCommand))
    invoker.children[0].children[0].add(ComputerMacroInvoker(osCommand))
    invoker.display(1)
