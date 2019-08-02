import webapp2
import logging
#step 1: import jinja2 and os
import jinja2
import os

#Step 2: Set up Jinja Environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Email(object):
    def __init__(self, subject, unread):
        self.subject = subject
        self.unread = unread

    # def getSubject():
    #     return self.subject
    #
    # def isRead():
    #     if (self.unread == False):
    #         return " unread"
    #     else:
    #         return " read"

    def isSpam(self):
        if "free" in self.subject.lower() or "Click here" in self.subject.lower():
            return True
        return False

emails = [
    Email("Hey, how's it going", True),
    Email("Status report", False),
    Email("Click here for free servers!", True),
    Email("Free gift card for Spotify", True),
    Email("Registrar's office", False)
]

class MainPage(webapp2.RequestHandler):
    def get(self):
        spam = []
        nonSpam = []
        #Step 3: use the jinja environment to get our html
        for email in emails:
            if not email.isSpam():
                nonSpam.append(email)
            else:
                spam.append(email)

        template_vars = {
            "inbox": nonSpam,
            "spam": spam
        }
        template = jinja_env.get_template('templates/inbox.html')
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
