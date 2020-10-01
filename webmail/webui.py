from bottle import Bottle
from bottle import route, run, template, view

app=Bottle()

@app.get('/')
@app.get('/index.html')
@view('index')
def entry():
	return dict()

@app.get('/setting.html')
@view('setting')
def entry():
	return dict()

@app.get('/sendmail.html')
@view('sendmail')
def entry():
	return dict()

run(app=app, host='localhost', port=8081)
