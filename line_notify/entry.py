import os
from bottle import Bottle
from bottle import view, static_file

import line_notify_api

root = Bottle()

@root.get('/')
@root.get('/index.html')
@view('index')
def entry():
	return dict()

@root.get('/assets/<filepath:path>')
def readfile(filepath):
	rootpath=os.getcwd()+'/assets/'
	print (rootpath)
	print (filepath)
	return static_file(filepath, root=rootpath)

@root.get('/notify.html')
@view('notify')
def entry():
	return dict()

@root.get('/register.html')
@view('register')
def entry():
	return dict()

@root.get('/log.html')
@view('log')
def entry():
	return dict()

root.mount('/api/line_notify', line_notify_api.app)
root.run(host='localhost', port=8081, debug=True, reloader=True)
