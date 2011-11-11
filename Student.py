# -*- coding: utf-8 -*-
import os
import Login
import urlparse, urllib, urllib2
import BeautifulSoup

class Student:
    def __init__(self, name, fileLink, gradeLink):
        self.name = name
        self.fileLink = fileLink
        self.gradeLink = gradeLink
        self.getIds()

    def __str__(self):
        s = "%s\n%s\n%s" % (self.name, self.fileLink, self.gradeLink)
        return s

    def getIds(self):
        url = urlparse.urlparse(self.gradeLink)
        get = url.query.split('&')
        params = []
        for p in get:
            params.append(p.split('='))

        for p in params:
            if p[0] == 'id':
                self.id = p[1]
            elif p[0] == 'userid':
                self.userid = p[1]

    def createDir(self, basedir):
        Dir = basedir + self.name.replace(' ', '_')
        os.system("mkdir -p %s" % Dir)

    def downloadFile(self, login, basedir):
        path = basedir + self.name.replace(' ', '_')
        fileName = self.fileLink.split('/')[-1]
        localFilePath = path + '/' + fileName
        print localFilePath
        data = login.open(self.fileLink)
        localFile = open(localFilePath, 'w')
        localFile.write(data)
        localFile.close()

    def reviewNaoEntregou(self, login, subPage):
        page = login.open(self.gradeLink)
        soup = BeautifulSoup.BeautifulSoup(page)
        #all inputs
        inputs = soup.findAll('input')
        params = {}
        
        for i in inputs:
            if i['type'] == 'hidden' and i.has_key('name'):
                params[i['name']] = i['value']

        params['xgrade'] = -1
        params['submissioncomment_editor[text]'] = 'Nao entregou'

#        print params

        inputData = urllib.urlencode(params)
        resp = login.sendData(subPage, inputData)

    def copyFile(self, fromPath, basePath, fileName):
        path = basePath + self.name.replace(' ', '_') + '/' + fileName
        os.system('cp %s %s' % (fromPath, path))

    def reviewEntregou(self, login, subPage, nota, comments):
        page = login.open(self.gradeLink)
        soup = BeautifulSoup.BeautifulSoup(page)
        #all inputs
        inputs = soup.findAll('input')
        params = {}
        
        for i in inputs:
            if i['type'] == 'hidden' and i.has_key('name'):
                params[i['name']] = i['value']

        params['xgrade'] = str(nota)
        params['submissioncomment_editor[text]'] = comments

#        print params

        inputData = urllib.urlencode(params)
        resp = login.sendData(subPage, inputData)


