# -*- coding:utf-8 -*-
# Copyright (C) 2017- TrafficSim Co.,Ltd. All rights reserved.

import os
import json,random

from bottle import get, post, request, response
from bottle import view,template,static_file

@get('/')
@get('/index.html')
@view('fruits')
def entry():
	return dict(message="hello bottle")

@get('/assets/<filepath:path>')
def readfile(filepath):
	rootpath = os.getcwd()+'/assets/'
	print (rootpath)
	print (filepath)
	return static_file(filepath, root=rootpath)

if __name__ == '__main__':
	run(host='0.0.0.0', port=8081)
else:
	application = default_app()

import fruits

import movpost

import picpost
