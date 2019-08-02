import webapp2
import logging
#step 1: import jinja2 and os
import jinja2
import os

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/start.html")
        self.response.write(template.render())

class Run(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/run.html")
        self.response.write(template.render())

class Enter(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/enter.html")
        self.response.write(template.render())

class Selfie(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/selfie.html")
        self.response.write(template.render())

class Cops(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/911.html")
        self.response.write(template.render())

class Faster(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/faster.html")
        self.response.write(template.render())

class Hide(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/hide.html")
        self.response.write(template.render())

class Store(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/store.html")
        self.response.write(template.render())

class Wait(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/wait.html")
        self.response.write(template.render())

class TJay(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/tjay.html")
        self.response.write(template.render())

class TJayCops(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/tjaycops.html")
        self.response.write(template.render())

class Baseball(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/baseball.html")
        self.response.write(template.render())

class School(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/school.html")
        self.response.write(template.render())

class Panic(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/panic.html")
        self.response.write(template.render())

class Silence(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/silence.html")
        self.response.write(template.render())

class Talk(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/talk.html")
        self.response.write(template.render())

class Stupid(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/stupid.html")
        self.response.write(template.render())

class Elsewhere(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/elsewhere.html")
        self.response.write(template.render())

class Slow(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/slow.html")
        self.response.write(template.render())

class Force(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/force.html")
        self.response.write(template.render())

class Dim(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/dim.html")
        self.response.write(template.render())

class Hum(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/hum.html")
        self.response.write(template.render())

class Silence(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/silence.html")
        self.response.write(template.render())

class License(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/license.html")
        self.response.write(template.render())

class Apology(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/apology.html")
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/run", Run),
    ("/enter", Enter),
    ("/selfie", Selfie),
    ("/911", Cops),
    ("/faster", Faster),
    ("/tjay", TJay),
    ("/hide", Hide),
    ("/enter", Enter),
    ("/store", Store),
    ("/baseball", Baseball),
    ("/school", School),
    ("/panic", Panic),
    ("/silence", Silence)
], debug = True)
