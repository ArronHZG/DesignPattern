# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 单例模式.py
@time: 2017/12/24 0024 14:57

单例模式（Singleton Pattern）是 Java 中最简单的设计模式之一。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。
这种模式涉及到一个单一的类，该类负责创建自己的对象，同时确保只有单个对象被创建。这个类提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象。
注意：
1、单例类只能有一个实例。
2、单例类必须自己创建自己的唯一实例。
3、单例类必须给所有其他对象提供这一实例。
介绍
意图：保证一个类仅有一个实例，并提供一个访问它的全局访问点。
主要解决：一个全局使用的类频繁地创建与销毁。
何时使用：当您想控制实例数目，节省系统资源的时候。
如何解决：判断系统是否已经有这个单例，如果有则返回，如果没有则创建。
关键代码：构造函数是私有的。
应用实例： 1、一个党只能有一个主席。 2、Windows 是多进程多线程的，在操作一个文件的时候，就不可避免地出现多个进程或线程同时操作一个文件的现象，所以所有文件的处理必须通过唯一的实例来进行。 3、一些设备管理器常常设计为单例模式，比如一个电脑有两台打印机，在输出的时候就要处理不能两台打印机打印同一个文件。
优点： 1、在内存里只有一个实例，减少了内存的开销，尤其是频繁的创建和销毁实例（比如管理学院首页页面缓存）。 2、避免对资源的多重占用（比如写文件操作）。
缺点：没有接口，不能继承，与单一职责原则冲突，一个类应该只关心内部逻辑，而不关心外面怎么样来实例化。
使用场景： 1、要求生产唯一序列号。 2、WEB 中的计数器，不用每次刷新都在数据库里加一次，用单例先缓存起来。 3、创建的一个对象需要消耗的资源过多，比如 I/O 与数据库的连接等。
注意事项：getInstance() 方法中需要使用同步锁 synchronized (Singleton.class) 防止多线程同时进入造成 instance 被多次实例化。
https://www.cnblogs.com/linxiyue/p/3902256.html

__new__   http://www.cnblogs.com/ifantastic/p/3175735.html  https://www.cnblogs.com/tuzkee/p/3540293.html
super http://blog.csdn.net/tab_space/article/details/50506138

'''
# class Singleton(object):
#     __instance=None
#     def __init__(self):
#         pass
#     def __new__(cls,*args,**kwd):
#         if Singleton.__instance is None:
#             Singleton.__instance=object.__new__(cls,*args,**kwd)
#         return Singleton.__instance

# class Singleton():
#     def __new__(cls,*args,**kwargs):
#         if not hasattr(cls,'__inst'):
#             cls.__inst=object().__new__(cls,*args,**kwargs)
#         return cls.__inst

class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print(cls)
            print(cls.__class__.mro(cls))
            print(super())
            print(super(Singleton,cls))
            print(super(object, cls))
            cls._instance = super(cls.__class__,cls).__new__(cls)
        return cls._instance

class A(Singleton):
    def __init__(self,s):
        self.s=s
if __name__=='__main__':
    print(A._instance)
    a=A('apple')
    print(id(a), a.s)
    b=A('banana')
    print(id(a),a.s)
    print(id(b),b.s)
    print(super(a.__class__))
    print(a.__class__.mro())
    print(A._instance)