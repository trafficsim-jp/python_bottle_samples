import os
import json

from bottle import get, post
from bottle import view, template

@get('/webcam')
@view('webcam')
def entry():
	return dict(message="hello,bottle")
