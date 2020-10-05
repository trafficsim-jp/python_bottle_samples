# -*- coding: utf-8 -*-
import sys,os,datetime,json

from bottle import Bottle
from bottle import get, post, request, response

# 注意 Python3ではurllibの使い方が違います
import urllib,urllib2
import http_settings

CONFIG_JSON_PATH=os.getcwd()+'/line_notify_conf.json'
LOG_FILE_PATH=os.getcwd()+'/line_notify.log'

LINE_NOTIFY_APIURI = 'https://notify-api.line.me/api/notify'

def load_config_file():
	conf_obj = {}

	try:
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_obj = json.load(f)
	except IOError as e:
		pass
	except JSONDecodeError as e:
		pass
	finally:
		pass

	return conf_obj

def output_log(message):
	output_message=str(datetime.datetime.now())+","+message
	with open(LOG_FILE_PATH, mode='a') as f:
		f.write(output_message+'\n')

app = Bottle()
app.add_hook('after_request', http_settings.enable_cors)

@app.post('/notify')
def entry():
	# LINE グループへの投稿
	try:
		conf_obj = load_config_file();
		payload = {'message' : 'current notify test'}
		payload = urllib.urlencode(payload).encode("utf-8")
		req = urllib2.Request(LINE_NOTIFY_APIURI)
		req.add_header('Content-Type', 'application/x-www-form-urlencoded')
		req.add_header('Authorization', 'Bearer ' + conf_obj['access_token'].strip())
		req.add_data(payload)

		resp_handler = urllib2.urlopen(req)
		resp = resp_handler.read()
		print (resp)

	except KeyError as e:
		response.status = 500
		response.content_type = 'application/json'
		return json.dumps({'error' : e.message + " is missing"})

	except:
		#print "Unexpect except:",sys.exc_info()[0]
		#print "Unexpect except:",sys.exc_info()[1]
		response.content_type = 'application/json'
		return json.dumps({'error' : sys.exc_info()[1]})

	return json.dumps({"result" : "success"})

@app.get('/access_token')
def entry():
	access_token=""
	try:
		conf_obj = load_config_file()
		access_token = conf_obj['access_token']

	except IOError as e:
		if (e.errno == 2):
			# まだ設定されていない.
			response.status = 404
			response.content_type = 'application/json'
			return json.dumps({'error' : 'not found'})
		else:
			# 何らかのErrorで読めない
			response.status = 500
			response.content_type = 'application/json'
			return json.dumps({'error' : e.message})
	except KeyError:
		response.status = 500
		response.content_type = 'application/json'
		return json.dumps({'error' : e.message})
	finally:
		pass

	return json.dumps({"access_token": access_token})

@app.post('/access_token')
def entry():

	try:
		conf_obj = load_config_file()
		conf_obj['access_token'] = request.json['access_token']
		with open(CONFIG_JSON_PATH, mode='w') as f:
			json.dump(conf_obj, f)

	except IOError as e:
		response.status = 500
		response.content_type = 'application/json'
		return json.dumps({'error' : e.message})

	except KeyError:
		response.status = 400
		response.content_type = 'application/json'
		return json.dumps({'error' : 'invalid format'})

	return json.dumps({"result": "success"})
