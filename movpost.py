import os
import json
import base64

from bottle import get, post, request, response
from bottle import view, template, route, static_file

@get('/movpost')
@view('movpost')
def entry():
	return dict(message="hello,bottle")
