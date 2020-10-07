import random
import string

import cherrypy


class StringGenerator(object):
  @cherrypy.expose
  def index(self):
    return """<html>
      <head></head>
      <body>
        <form method="get" action="generate">
          <input type="text" value="8" name="length" />
          <button type="submit">Give me da hex code now!</button>
        </form>
      </body>
    </html>"""

  @cherrypy.expose
  def generate(self, length=8):
    some_string = ''.join(random.sample(string.hexdigits, int(length)))
    cherrypy.session['mystring'] = some_string
    return some_string

  @cherrypy.expose
  def display(self):
    return cherrypy.session['mystring']


if __name__ == '__main__':
  conf = {
    '/': {
      'tools.sessions.on': True
    }
  }
  ###lines 30-34 show you how to enable the session support in your CherryPy application. By default, CherryPy will save sessions in the process’s memory. It supports more persistent backends as well.####
  cherrypy.config.update("server.conf")
  cherrypy.quickstart(StringGenerator(), '/', conf)

  