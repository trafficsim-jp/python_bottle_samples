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
