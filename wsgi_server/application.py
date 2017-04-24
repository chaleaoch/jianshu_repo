#!/usr/bin/env python
# -*- coding: utf-8 -*-

def application(environ, start_response):
    '''
    @param environ:dict,包含了很多http相关的环境变量
    @param start_response:一个函数
    @return: 一个可迭代对象
    '''
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world1']