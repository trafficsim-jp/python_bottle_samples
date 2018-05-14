from bottle import get

from bottle import view, template

@get('/record')
@view('record')
def entry():
	return dict(message="hello, bottle")
