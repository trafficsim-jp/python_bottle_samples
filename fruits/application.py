# -*- coding:utf-8 -*-
# Copyright (C) 2017- TrafficSim Co.,Ltd. All rights reserved.

import os
import json,random

from bottle import get
from bottle import view,template,static_file

@get('/')
@get('/index.html')
@view('index')
def entry():
    return dict(message="hello bottle")

@get('/assets/<filepath:path>')
def readfile(filepath):
    rootpath = os.getcwd()+'/assets/'
    print rootpath
    print filepath
    return static_file(filepath, root=rootpath)

@get('/api/fruits')
def entry():

    random.seed();

    furits = ['apple', 'oringe', 'mango', 'strawberry', 'rasiberry', 'peach' ];
    respmsg = { "fruits" : furits[random.randint(0, 5)] }

    return json.dumps(respmsg, ensure_ascii=False)
