import os
from bottle import Bottle
from bottle import view, static_file

import sendmail_api

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

@root.get('/setting.html')
@view('setting')
def entry():
	return dict()

@root.get('/sendmail.html')
@view('sendmail')
def entry():
	return dict()

@root.get('/log.html')
@view('log')
def entry():
	return dict()

root.mount('/api/sendmail', sendmail_api.app)
root.run(host='localhost', port=8081, debug=True, reloader=True)

