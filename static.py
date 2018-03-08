from bottle import route, static_file, get

@get('/api/<file_path:path>')
def static(file_path):
    return static_file(file_path, root='./')
