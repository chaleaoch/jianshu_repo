#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-
class LazyProxy(object):
    def __init__(self, cls, *args, **kwargs):
        self.__dict__['_cls'] = cls
        self.__dict__['_params'] = args
        self.__dict__['_kwargs'] = kwargs
        self.__dict__["_obj"] = None

    def __getattr__(self, item):
        if self.__dict__['_obj'] is None:
            self._init_obj()
        return getattr(self.__dict__['_obj'], item)

    def __setattr__(self, key, value):
        if self.__dict__['_obj'] is None:
            self._init_obj()
        setattr(self.__dict__['_obj'], key, value)

    def _init_obj(self):
        self.__dict__['_obj'] = object.__new__(self.__dict__['_cls'],
                                               *self.__dict__['_params'],
                                               **self.__dict__['_kwargs'])
        self.__dict__['_obj'].__init__(*self.__dict__['_params'],
                                       **self.__dict__['_kwargs'])

class LazyInit(object):
    def __new__(cls, *args, **kwargs):
        return LazyProxy(cls, *args, **kwargs)

class A(LazyInit):
    def __init__(self, x):
        # 因为__new__返回的实例不是A的，所以__init__并不会被type执行
        print ("Init A")
        self.x = 14 + x

a = A(1)
print "Go"
print a.x