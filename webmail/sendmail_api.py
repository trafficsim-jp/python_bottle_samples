# -*- coding: utf-8 -*-
import os,json

from bottle import Bottle
from bottle import get, post, request, response

import http_settings

CONFIG_JSON_PATH=os.getcwd()+'/sendmail_conf.json'

def load_config_file():
	conf_obj = {}
	# 例外の処理はときに行わない.
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

app = Bottle()
app.add_hook('after_request', http_settings.enable_cors)

@app.get('/smtp_server')
def entry():
	smtp_server=""
	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json.load(f)
			print(conf_json)
			smtp_server=conf_json['smtp_server']

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

	return json.dumps({"smtp_server": smtp_server})

@app.post('/smtp_server')
def entry():
	print(request.json)

	try:
		print(request.json['smtp_server'])
		conf_obj = load_config_file();
		conf_obj['smtp_server'] = request.json['smtp_server']
		with open(CONFIG_JSON_PATH, mode='w') as f:
			json.dump(conf_obj,f)

	except IOError as e:
		response.status = 500
		response.content_type = 'application/json'
		return json.dumps({'error' : e.message})

	except KeyError:
		response.status = 400
		response.content_type = 'application/json'
		return json.dumps({'error' : 'invalid format'})

	return json.dumps({"result": "success"})

@app.get('/smtp_server_port')
def entry():
	port=0
	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json.load(f)
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
			conf_json = json.load(f)
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
			conf_json = json.load(f)
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
			conf_json = json.load(f)
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
	dest_addresses=""
	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json.load(f)
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
