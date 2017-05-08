#!/usr/bin/env python
# -*- coding: utf-8 -*-
class lazy_property(object):
    def __init__(self, func, name=None, doc=None):
        self._func = func
        self._name = name or func.func_name
        self.__doc__ = doc or func.__doc__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self._func(obj)
        setattr(obj, self._name, value)
        return value

class BaseRequest(object):
    def form(self):
        return 123
    form = lazy_property(form)

bb = BaseRequest()
print bb.form
print bb.form
bb = BaseRequest()
print bb.form
print bb.form