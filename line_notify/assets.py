import os
from bottle import request
def assets(type,path):
	assetspath=os.getcwd()+'/assets/%s/%s' % (type,path)
	url='<script src="%s://%s/assets/%s/%s?%s"></script>' % (request.urlparts.scheme, request.urlparts.netloc,type,path,str(int(os.path.getmtime(assetspath))))
	return url
