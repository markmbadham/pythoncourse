#!/usr/bin/env python
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    d = {
        'name':'fred',
        'surname':'bloggs',
        'age':10
    }
    ret = [
        "<!DOCTYPE html>\n",
        "<head><title>HelloWorld</title></head>\n",
        "<body>\n",
        "<h1>HelloWorld</h1>\n",
        "This is a standard Hello World page",
        "<table border=1>\n"]
    for key in d:
        ret.append("<tr><td>%s</td><td>%s</td></tr>" % (key,d[key]))
    ret += [
        "</table>",
        "</body>\n",
        "</html>\n"
        ]
    return ret
httpd = make_server('', 8000, simple_app)
print "Serving on port 8000..."
httpd.serve_forever()


