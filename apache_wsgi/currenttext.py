import os
import json

from bottle import get, response
from bottle import view, template

@get('/currenttext')
@view('currenttext')
def entry():
	return dict(message="hello bottle")

@get('/api/currenttext')
def entry():

	inputfile = os.getcwd()+'/outpost.txt'
	outposts = open(inputfile,'r')
	outpost = outposts.read()
	response.set_header("Content-Type", "application/json;charset=UTF-8")
	respmsg = { "currenttext" : outpost }

	return json.dumps(respmsg, ensure_ascii=False)
