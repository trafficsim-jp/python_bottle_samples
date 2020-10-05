# -*- coding: utf-8 -*-
import os,datetime,json

from bottle import Bottle
from bottle import get, post, request, response

import http_settings
import smtplib_wrapper

CONFIG_JSON_PATH=os.getcwd()+'/sendmail_conf.json'
LOG_FILE_PATH=os.getcwd()+'/sendmail.log'

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

def output_log(message):
	output_message=str(datetime.datetime.now())+","+message
	with open(LOG_FILE_PATH, mode='a') as f:
		f.write(output_message+'\n')

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
	try:
		conf_obj = load_config_file()
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
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json.load(f)
			port = conf_json['smtp_server_port']

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
		# 設定がされていない
		response.status = 404
		response.content_type = 'application/json'
		return json.dumps({'error' : 'not found'})

	finally:
		pass

	return json.dumps({"smtp_server_port": port})

@app.post('/smtp_server_port')
def entry():

	try:
		conf_obj = load_config_file();
		conf_obj['smtp_server_port'] = request.json['smtp_server_port']
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

@app.get('/username')
def entry():
	username=""

	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json.load(f)
			username = conf_json['username']

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

@app.post('/username')
def entry():

	try:
		conf_obj = load_config_file();
		conf_obj['username'] = request.json['username']
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

@app.get('/password')
def entry():

	password=""
	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json.load(f)
			password=conf_json['password']

	except KeyError:
		pass

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

@app.post('/password')
def entry():

	try:
		conf_obj = load_config_file();
		conf_obj['password'] = request.json['password']
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

@app.get('/from_address')
def entry():

	from_address=""

	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json.load(f)
			from_address = conf_json['from_address']

	except KeyError:
		pass

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

@app.post('/from_address')
def entry():
	try:
		conf_obj = load_config_file();
		conf_obj['from_address'] = request.json['from_address']
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

@app.get('/dest_addresses')
def entry():
	dest_addresses=""

	try:
		print(CONFIG_JSON_PATH)
		with open(CONFIG_JSON_PATH, mode='r') as f:
			conf_json = json.load(f)
			dest_addresses = conf_json['dest_addresses']

	except KeyError:
		pass

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

@app.post('/dest_addresses')
def entry():
	try:
		conf_obj = load_config_file();
		conf_obj['dest_addresses'] = request.json['dest_addresses']
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

@app.post('/sendmessage')
def entry():
	# メールメッセージの送信
	try:
		conf_obj = load_config_file();
		msg = smtplib_wrapper.create_message(conf_obj['from_address'],
											 conf_obj['dest_addresses'],
											 request.json['subject'],
											 request.json['message']);

		result = smtplib_wrapper.sendmail(conf_obj['smtp_server'],
										  conf_obj['smtp_server_port'],
										  conf_obj['username'],
										  conf_obj['password'],
										  conf_obj['from_address'],
										  conf_obj['dest_addresses'].split(','),
										  msg)
		if result != "success":
			output_log(result)
			response.status = 500
			response.content_type = 'application/json'
			return json.dumps({'error' : result.split(':')[1]})

	except KeyError:
		response.status = 409
		response.content_type = 'application/json'
		output_log("error: invalid condition")
		return json.dumps({'error' : 'invalid condition'})

	output_log("success: to "+conf_obj['dest_addresses'])

	return json.dumps({"result": "success"})

@app.get('/log')
def entry():

	try:
		with open(LOG_FILE_PATH,mode="r") as f:
			log = f.read()
			return json.dumps({"log": log})

	except IOError as (err,msg):
		if err == 2:
			return json.dumps({"log": ""})
		else:
			response.status = 500
			response.content_type = 'application/json'
			return json.dumps({'error' : 'internal error'})
