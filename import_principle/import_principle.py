#!/usr/bin/env python
# -*- coding: utf-8 -*-

import module_a

module_a.module_b.function_b()
# module_b.function_b()会报错

import package_a #不会打印package_a_module_a
import package_a.package_a_module_a #会打印package_a_module_a

'''
from <module> import <object>
相当于
import module
<object> = module.<object>
del module
'''
package_a.package_a_module_a_function_a()
