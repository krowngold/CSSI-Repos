import webapp2
import logging
#step 1: import jinja2 and os
import jinja2
import os

#Step 2: Set up Jinja Environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/madlibs.html')
        self.response.write(template.render())

    def post(self):
        templates_var = {
            "tallAdj": self.request.get("tallAdj"),
            "niceBuildingAdj": self.request.get("niceBuildingAdj"),
            "niceAdj": self.request.get("niceAdj"),
            "smithName": self.request.get("smithName"),
            "animalName": self.request.get("animalName"),
            "weirdFood": self.request.get("weirdFood"),
            "vehicle": self.request.get("vehicle"),
        }
        template = jinja_env.get_template('templates/story.html')
        self.response.write(template.render(templates_var))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
