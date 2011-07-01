import urllib, urllib2, cookielib

class Login:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.cookieJar = cookielib.CookieJar()
        self.opener = urllib2.build_opener(
                urllib2.HTTPCookieProcessor(self.cookieJar))
        
    def connect(self, fieldusername, fieldpassword):
        self.loginData = urllib.urlencode({fieldusername : self.user,
            fieldpassword : self.password})

        self.opener.open('http://paca.ime.usp.br/login/index.php', 
                self.loginData)
        self.opener.close()
        print "Connection Ok"

    def open(self, url):
        self.response = self.opener.open(url)
        self.data = self.response.read()
        self.response.close()
        return self.data

    def sendData(self, url, data):
        self.request = urllib2.Request(url, data);
        self.response = self.opener.open(self.request)
        self.data = self.response.read()
        return self.data
