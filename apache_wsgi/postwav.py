import os
import json
from datetime import datetime

from bottle import get, post, request, response
from bottle import view, template, route, static_file

@post('/api/postwav')
def receiveWAV():

	filename = "upload.wav"
	upload = request.files.get('upload')
	name, ext = os.path.splitext(upload.filename)


	if ext not in ('.wav'):
		return "File extension not allowed."

	save_path = "./"
	upload.filename = filename
	file_path = "{path}/{file}".format(path=save_path, file=upload.filename)

	upload.save("./",overwrite=True)
	return json.dumps({"savefile":filename})

@get('/getwav/<filename>')
def send_image(filename):
	return static_file(filename, root='', mimetype='audio/wav')
