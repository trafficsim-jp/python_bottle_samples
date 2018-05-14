import os
import json

from bottle import get, post, request, response
from bottle import view, template

@get('/posttest')
@view('posttest')
def entry():
	return dict(message="hello bottle")

@post('/api/posttest')
def entry():
	outputfile = os.getcwd()+'/outpost.txt'
	empty = {}
	body = request.body.read()
	outputf = open(outputfile,'w')
	outputf.write(body)
	outputf.close()
	response.status = 200
	response.set_header("Content-Type", "application/json;charset=UTF-8")
	return json.dumps({})
