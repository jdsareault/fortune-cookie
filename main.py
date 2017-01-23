import webapp2
import random

def getRandomFortune():
    fortunelist = [
        "I see much code in your future",
        "Consider eating more fortune cookies",
        "Only listen to the fortune cookie, diregard all other fortune telling units",
        "Help! I'm being held prisoner in a Chinese bakery!",
        "You will read this and say 'Geez! I can write better fortunes than that!'",
        "You are not illiterate",
        "A foolish man listens to his heart. A wise man listens to cookies"
    ]

    nextFortune = random.choice(fortunelist)

    return nextFortune

class Index(webapp2.RequestHandler):
    def get(self):
        luckyNum = random.randint(1,100)
        header = "<h1> Fortune Cookie</h1>"

        fortune = getRandomFortune()
        fortuneSentence = "Your fortune: <strong>" + str(getRandomFortune()) + "</strong>"
        fortuneParagraph = "<p>" + fortuneSentence + "</p>"

        numSentence = "Your Lucky Number is <strong>" + str(luckyNum) + "</strong>"
        numParagraph = "<p>" + numSentence + "</p>"

        newFortuneButton = "<a href='.'><button>Another Cookie, Please</button></a>"

        content = header + fortuneParagraph + numParagraph + newFortuneButton
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
