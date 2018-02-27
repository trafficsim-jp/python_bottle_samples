import os
import json
import base64

from bottle import get, response
from bottle import view, template

@get('/getmovpost')
@view('getmovpost')
def entry():
	return dict(message="hello,bottle")

@get('/api/getmovpost')
def entry():

	inputfile = os.getcwd()+'/movpost.jpeg'
	outposts = open(inputfile,'r')
	outpost = outposts.read()
	encbody = base64.b64encode(outpost)
	response.set_header("Content-Type", "application/json;charset=UTF-8")
	respmsg = { "currentmov" : encbody }

	return json.dumps(respmsg, ensure_ascii=False)
