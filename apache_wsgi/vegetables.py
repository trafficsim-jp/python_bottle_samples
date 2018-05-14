import json, random

from bottle import get
from bottle import view, template

@get('/vegetables')
@view('vegetables')
def entry():
	return dict(message="hello bottle")

@get('/api/vegetables')
def entry():

	random.seed();

	vegetables = ['tomato', 'carrot', 'potato', 'onion', 'cucumber', 'cabbage' ];
	respmsg = { "vegetables" : vegetables[random.randint(0, 5)] }

	return json.dumps(respmsg, ensure_ascii=False)
