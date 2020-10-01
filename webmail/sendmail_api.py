import json

from bottle import Bottle
from bottle import get, post

import http_settings

app = Bottle()
app.add_hook('after_request', http_settings.enable_cors)

@app.get('/username')
def entry():
	return json.dumps({"username" : "" })

