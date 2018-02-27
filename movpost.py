import os
import json
import base64

from bottle import get, post, request, response
from bottle import view, template, route, static_file

@get('/movpost')
@view('movpost')
def entry():
	return dict(message="hello,bottle")

@post('/api/picpost')
def entry():
	outputfile = os.getcwd()+'/picpost.jpeg'
	empty = {}
	picture = request.json["picture"]
	bodies = picture.split(",")
	body = bodies[-1]
	decbody = base64.b64decode(body)
	outputf = open(outputfile,'w')
	outputf.write(decbody)
	outputf.close()
	response.status = 200
	response.set_header("Content-Type", "application/json;charset=UTF-8")
	return json.dumps({})
