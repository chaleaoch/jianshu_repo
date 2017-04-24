#!/usr/bin/env python
# -*- coding: utf-8 -*-

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world1']