import webapp2
import logging
import jinja2
import datetime
import os
from google.appengine.api import users

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

from google.appengine.ext import ndb

class Star(ndb.Model):
    """
    name: String for the star's name
    birthday: Date for the star's birthday
    hometown: String for the star's hometown
    avgrating: float for the star's avg composite movie rating online (0.0-10.0)
    gender: M, F, or N/A
    """

    name = ndb.StringProperty(required=True)
    oscars = ndb.IntegerProperty(required=False, default = 0)
    gender = ndb.StringProperty(required=True)
    pronoun = ndb.StringProperty(required=False, default = "")

class Movie(ndb.Model):
    """
    title: String for the movie title
    runtime: Number of minutes of the Movie
    rating: from 0-10
    """

    title = ndb.StringProperty(required=True)
    runtime = ndb.IntegerProperty(required=True)
    rating = ndb.FloatProperty(required=False, default = 0.0)
    releaseDate = ndb.DateProperty(required=True)
    star_keys = ndb.KeyProperty(kind=Star, required=False, repeated=True)

    def describe(self):
        return "%s has a runtime of %d minutes and received a rating of %f" % (self.title, self.runtime, self.rating)

class MainPage(webapp2.RequestHandler):
    def get(self):

        current_user = users.get_current_user()
        signin_link = users.create_login_url("/")

        star_list = Star.query().fetch()
        stars_oscars = {}
        for star in star_list:
            stars_oscars.update({star.name: star.oscars})
        print stars_oscars
        movie_query = Movie.query().filter(Movie.rating > 7).order(-Movie.rating)
        movie_list = movie_query.fetch()
        movies = []
        for movie in movie_list:
            movies.append(movie)

        print stars_oscars
        template_vars = {
            "movies":movies,
            "stars_oscars": stars_oscars,
            "current_user": current_user,
            "signin_link": signin_link,
        }
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render(template_vars))

class PopulateDatabase(webapp2.RequestHandler):
    def get(self):
        beyonce_key = Star(name="Beyonce", gender="F", oscars = 0).put()
        glover_key = Star(name="Donald Glover", gender="M", oscars = 0).put()
        rogen_key = Star(name="Seth Rogen", gender="M", oscars=0).put()
        oliver_key=Star(name="John Oliver", gender="M", oscars=0).put()
        dicaprio_key=Star(name="Leonardo DiCaprio", gender="M", oscars=6).put()
        pitt_key=Star(name="Brad Pitt", gender="M", oscars=6).put()
        robbie_key=Star(name="Margot Robbie", gender="F", oscars=20).put()

        hollywood = Movie(title="Once Upon a Time in Hollywood", runtime=165, rating=9.5, releaseDate=datetime.datetime(2019, 7, 26), star_keys = [
        pitt_key, robbie_key, dicaprio_key
        ]).put()
        # "Leonardo DiCaprio": 6,
        # "Brad Pitt": 6,
        # "Margot Robbie": 20})

        lion_king = Movie(title="Lion King", runtime = 118, rating=7.2, releaseDate=datetime.datetime(2019,7,19), star_keys = [
        # Star(name = "Beyonce", gender = "F", oscars = 0),
        # Star(name = "Donald Glover", gender = "M", oscars = 0),
        # Star(name = "Seth Rogen", gender = "M", oscars = 0),
        # Star(name = "John Oliver", gender = "M", oscars = 0)]
        beyonce_key, glover_key, rogen_key, oliver_key]).put()


        # CLASS TO BE USED WHENEVER DATABASE NEEDS NEW ENTRIES
        # UNCOMMENT POPULATE DATABASE LINK IN main.html AND PRESS LINK TO ADD ENTRIES
        # CREATE STAR AND MOVIE OBJECTS AND .put() THEM\

        self.redirect("/")

class ViewStars(webapp2.RequestHandler):
    def get(self):


        template = jinja_env.get_template('templates/viewstars.html')
        self.response.write(template.render(template_vars))

class PrintStars(webapp2.RequestHandler):
    def get(self):

        star_list = Star.query().fetch()
        template_vars = {
            "star_list": star_list
        }

        template = jinja_env.get_template('templates/stars.html')
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/populateDatabase', PopulateDatabase),
    ('/stars', PrintStars),
    ('/viewstars', ViewStars),
], debug=True)
