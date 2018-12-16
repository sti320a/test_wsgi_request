import cgi
from wsgiref.simple_server import make_server
import pprint

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    method = environ.get('REQUEST_METHOD')
    # contentの長さを取得する
    content_length = environ.get('CONTENT_LENGTH', 0)
    # 指定した長さの分だけファイルオブジェクトをreadする
    if method == 'POST':
        body = environ.get('wsgi.input').read(int(content_length))
        print('body: {}'.format(body))
    return ['Hello, World'.encode('utf-8')]

with make_server('', 8000, application) as httpd:
    httpd.serve_forever()