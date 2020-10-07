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
          <button type="submit">Give it now fr!</button>
        </form>
      </body>
    </html>"""
  
  @cherrypy.expose
  def generate(self, length=8):
    return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
  cherrypy.config.update("server.conf")
  cherrypy.quickstart(StringGenerator())
  ####Notice that in this example, the form uses the GET method and when you pressed the Give it now! button, the form is sent using the same URL as in the previous tutorial. HTML forms also support the POST method, in that case the query-string is not appended to the URL but it sent as the body of the client’s request to the server. However, this would not change your application’s exposed method because CherryPy handles both the same way and uses the exposed’s handler parameters to deal with the query-string (key, value) pairs.####