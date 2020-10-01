# -*- coding: utf-8 -*-
import os,json

from bottle import Bottle
from bottle import get, post, response

import http_settings

CONFIG_JSON_PATH=os.getcwd()+'/conf/sendmail_conf.json'

app = Bottle()
app.add_hook('after_request', http_settings.enable_cors)

@app.get('/smtp_server')
def entry():
	smtp_server=""
	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json_load(f)
			print(conf_json)
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
	finally:
		pass

	return json.dumps({"smtp_server": smtp_server})

@app.get('/smtp_server_port')
def entry():
	port=0
	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json_load(f)
			print(conf_json)
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
	finally:
		pass

	return json.dumps({"smtp_server_port": port})

@app.get('/username')
def entry():
	username=""

	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json_load(f)
			print(conf_json)

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
	finally:
		pass

	return json.dumps({"username" : username})


@app.get('/password')
def entry():

	password=""
	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json_load(f)
			print(conf_json)

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
	finally:
		pass

	return json.dumps({"password": password})

@app.get('/from_address')
def entry():
	from_address=""
	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json_load(f)
			print(conf_json)

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
	finally:
		pass

	return json.dumps({"from_address": from_address})

@app.get('/dest_addresses')
def entry():
	dest_address=""
	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json_load(f)
			print(conf_json)

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
	finally:
		pass

	return json.dumps({"dest_addresses": dest_addresses})
