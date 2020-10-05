# -*- coding: utf-8 -*-
import os,datetime,json

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
	print "POST notify"
	try:
		conf_obj = load_config_file();
		req_headers = {
			'Content-Type'  : 'application/x-www-form-urlencoded',
			'Authorization' : 'Bearer ' + ACCESS_TOKEN
		}
		payload = {'message' : 'current notify test'}
		payload = urllib.urlencode(payload).encode("utf-8")
		req = urllib2.Request(LINE_NOTIFY_APIURI)
		req.add_header('Content-Type', 'application/x-www-form-urlencoded')
		req.add_header('Authorization', 'Bearer ' + ACCESS_TOKEN)
		req.add_data(payload)

		resp_handler = urllib2.urlopen(req)
		resp = resp_handler.read()
		print (resp)

	except Exception as e:
		print "Exception Error:," , e

	return json.dumps({"result" : "success"})

