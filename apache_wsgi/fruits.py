import json, random

from bottle import get
from bottle import view, template

@get('/fruits')
@view('fruits')
def entry():
    return dict(message="hello bottle")

@get('/api/fruits')
def entry():

	random.seed();

	furits = ['apple', 'oringe', 'mango', 'strawberry', 'rasiberry', 'peach' ];
	respmsg = { "fruits" : furits[random.randint(0, 5)] }

	return json.dumps(respmsg, ensure_ascii=False)
