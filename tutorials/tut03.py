import random
import string

import cherrypy


class StringGenerator(object):
  @cherrypy.expose
  def index(self):
    return "Hello W ro ldregergg"

  @cherrypy.expose
  def generate(self, length=8):
    return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
  cherrypy.config.update("server.conf")
  cherrypy.quickstart(StringGenerator())
  ###In a URL such as this one, the section after ? is called a query-string. Traditionally, the query-string is used to contextualize the URL by passing a set of (key, value) pairs. The format for those pairs is key=value. Each pair being separated by a & character.

######Notice how we have to convert the given length value to an integer. Indeed, values are sent out from the client to our server as strings.

#####Much like CherryPy maps URL path segments to exposed functions, query-string keys are mapped to those exposed function parameters.