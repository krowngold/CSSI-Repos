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
    def post(self):
        fire = 0
        water = 0
        grass = 0
        normal = 0
        answer = "None"

        questions = [
            "activity",
            "weather",
            "transport",
            "animal",
            "sleep",
        ]

        for question in questions:
            selection = self.request.get(question)
            if (selection == "fire"):
                fire += 1
            elif (selection == "water"):
                water += 1
            elif (selection == "grass"):
                grass += 1
            else:
                normal +=1

        if (normal >= fire and normal >= water and normal >= grass):
            answer = "normal"
        if (fire >= water and fire >= grass and fire >= normal):
            answer = "fire"
        if (water >= fire and water >= grass and water >= normal):
            answer = "water"
        if (grass >= fire and grass >= water and grass >= normal):
            answer = "grass"

        template_vars = {
            "answer": answer,
        }
        template_vars.update()
        template = jinja_env.get_template("templates/results.html")
        self.response.write(template.render(template_vars))

    def get(self):
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render())

    # def findAnswer(self, results):
    #     max = 0
    #     current = 0
    #     for option in range(results.length-2):
    #         if (results[option] < results[option+1]):
    #             max = results[option+1]
    #
    #     return max


class FirstQPage(webapp2.RequestHandler):
    def get(self):
        template_vars = {

        }
        template = jinja_env.get_template('templates/question1.html')
        self.response.write(template.render(template_vars))

# class SecondQPage(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_env.get_template('templates/question2.html')
#         self.response.write(template.render())
#
# class ThirdQPage(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_env.get_template('templates/question3.html')
#         self.response.write(template.render())
#
# class FourthQPage(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_env.get_template('templates/question4.html')
#         self.response.write(template.render())
#
# class FifthQPage(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_env.get_template('templates/question5.html')
#         self.response.write(template.render())
#
# class ResultsPage(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_env.get_template('templates/results.html')
#         self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/question1', FirstQPage),
    # ('/question2', SecondQPage),
    # ('/question3', ThirdQPage),
    # ('/question4', FourthQPage),
    # ('/question5', FifthQPage),
    # ('/results', ResultsPage)
], debug=True)
