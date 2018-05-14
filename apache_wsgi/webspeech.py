from bottle import get

from bottle import view, template

@get('/webspeech')
@view('webspeech')
def entry():
	return dict(message="hello, bottle")
