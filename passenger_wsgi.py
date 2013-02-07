# Detailed explanation at http://hitesh.in/2011/running-a-bottle-py-app-on-dreamhost/
 
#1. Add current directory to path, if isn't already 
import os, sys
cmd_folder = os.path.dirname(os.path.abspath(__file__))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
 
import bottle
from bottle import route, run
 
#2. Define needed routes here	
@bottle.route('/wsgi')
def index():
	return "it works!"

import chromiumVersionReader

@bottle.route('/chromiumRevisionSelector')
def index():
    return str(chromiumVersionReader.findRevisionForOSAndChannel(bottle.request.query.os, bottle.request.query.channel))

	
#3. setup dreamhost passenger hook
def application(environ, start_response):
    return bottle.default_app().wsgi(environ,start_response)	
