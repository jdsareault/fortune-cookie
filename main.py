import webapp2
import random

class Index(webapp2.RequestHandler):
    def get(self):
        luckyNum = random.randint(1,100)
        header = "<h1> Fortune Cookie</h1>"
        numSentence = "Your Lucky Number is " + str(luckyNum)
        numParagraph = "<p>" + numSentence + </p>
        self.response.write(header + numParagraph)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
