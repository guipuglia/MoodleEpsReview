import urllib, urllib2, cookielib

class Login:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        print "Setted: %s %s" % (self.user, self.password)
        self.cookieJar = cookielib.CookieJar()
        self.opener = urllib2.build_opener(
                urllib2.HTTPCookieProcessor(self.cookieJar))
        
    def connect(self, fieldusername, fieldpassword):
        self.loginData = urllib.urlencode({fieldusername : self.user,
            fieldpassword : self.password})

        self.opener.open('http://paca.ime.usp.br/login/index.php', 
                self.loginData)
        print "Connection Ok"

    def open(self, url):
        self.response = self.opener.open(url)
        self.document = self.response.read()
        return self.document
