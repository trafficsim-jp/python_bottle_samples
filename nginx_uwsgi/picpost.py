import os
import json
import base64
import subprocess, shutil

import bottle
from bottle import get, post, request, response
from bottle import view, template, route, static_file

bottle.BaseRequest.MEMFILE_MAX = 4 * 1024 * 1024

@get('/picpost')
@view('picpost')
def entry():
	return dict(message="hello,bottle")

@post('/api/launch_darknet')
def entry():
	outputfile = os.getcwd()+'/picpost.jpeg'
	empty = {}
	picture = request.json["picture"]
	bodies = picture.split(",")
	body = bodies[-1]
	header = bodies[-2]
	decbody = base64.b64decode(body)
	outputf = open(outputfile,'wb')
	outputf.write(decbody)
	outputf.close()

	current_dir = os.getcwd()
	os.chdir("/local_home/iwata/git/darknet")
	cmd = "./darknet detect cfg/yolov3.cfg yolov3.weights %s -out detect" % outputfile
	#cmd = "./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights %s -out detect" % outputfile
	subprocess.call(cmd.split())
	os.chdir(current_dir)
	shutil.copy("/local_home/iwata/git/darknet/detect.jpg", "post_picpost.jpg")

	file = open('post_picpost.jpg','rb').read()
	enc_file = base64.b64encode(file)
	res = enc_file.decode("UTF-8")
	resp = header + "," + res

	response.status = 200
	response.set_header("Content-Type", "application/json;charset=UTF-8")

	return json.dumps(resp)
