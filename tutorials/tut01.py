import cherrypy

cherrypy.config.update("server.conf")
class HelloWorld(object):
  @cherrypy.expose
  def index(self):
    return "Hello World!"


if __name__ == '__main__':
  cherrypy.quickstart(HelloWorld())
  ###Look at console logs, then read the following:
  #The first three lines indicate the server will handle signal for you. 
  #The next line tells you the current state of the server, as that point it is in STARTING stage. 
  #Then, you are notified your application has no specific configuration set to it. 
  #Next, the server starts a couple of internal utilities that we will explain later.
  #Finally, the server indicates it is now ready to accept incoming communications as it listens on the address 127.0.0.1:8080. In other words, at that stage your application is ready to be used.