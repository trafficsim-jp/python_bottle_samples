# -*- Python -*-
# coding: utf-8
# Copyright (C) 2017- TrafficSim Co.,Ltd. All rights reserved.

# httpdからの起動の場合 /tmpはPrivateTmpで処理される.

import sys,os
import bottle

dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath)
os.chdir(dirpath)

import application

application = bottle.default_app()

def application(env, start_resp):
    app = bottle.default_app()
    return app(env, start_resp)

#def application(environ, start_response):

#    start_response('404 NOT FOUND', [('Content-type', 'text/plain')])

#    return 'Hello, world'
