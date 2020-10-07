import random
import string

import cherrypy


class StringGenerator(object):
  @cherrypy.expose
  def index(self):
    return "Hello World!!!"

  @cherrypy.expose
  def generate(self):
    return ''.join(random.sample(string.hexdigits, 16))


if __name__== '__main__':
  cherrypy.config.update("server.conf")
  cherrypy.quickstart(StringGenerator())
  
###Let’s take a minute to decompose what’s happening here. This is the URL that you have typed into your browser: http://localhost:8080/generate in Repl.it's case this is http://0.0.0.0:9090

##This URL contains various parts:

##http:// which roughly indicates it’s a URL using the HTTP protocol (see RFC 2616).

##localhost:8080 is the server’s address. It’s made of a hostname and a port.

##/generate which is the path segment of the URL. This is what CherryPy uses to locate an exposed function or method to respond.

###Here CherryPy uses the index() method to handle / and the generate() method to handle /generate