# -*- coding: utf-8 -*-

import BeautifulSoup
import unicodedata
import Student

import pdb

def strip_accents(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

class Parser:
    def __init__(self, document):
        self.document = document
        self.soup = BeautifulSoup.BeautifulSoup(self.document)

    def clean(self, htmltag, htmlprop, propName):
        table = self.soup.find(htmltag, {htmlprop: propName})
        return table

    def getStudents(self, table):
        rows = table.findAll('tr')

        del rows[0]

        res = []

        for row in rows:
            tdName = row.find('td', {'class': 'cell c1 fullname'})
            name = strip_accents(tdName.find('a').contents[0])
            
            tdFile = row.find('td', {'class': 'cell c4 timemodified'})
            if tdFile.find('a') is not None:
                fileLink = tdFile.find('a')['href']
            else:
                fileLink = ''
            
            tdStatus = row.find('td', {'class': 'cell c6 status'})
            statusLink = tdStatus.find('a')['href']

            res.append(Student.Student(name, fileLink, statusLink))
        return res

    def getResults(self, pathFile):
            f = open(pathFile, 'r')
            self.document = f.read()
#            print self.document
            state = 0
            sum = 0.0
            string = ''
            for c in self.document:
                if c == '|':
                    if state == 0:
                        state = 1
                    elif state == 1:
                        state = 2
                    elif state == 2:
                        sum += float(string)
                        string = ''
                        state = 0
                elif state == 1:
                    state = 0
                elif state == 2:
                    string += c

            return int(sum*10), self.document

    def getCelulas(self, linha):
        def dump(obj):
            for attr in dir(obj):
                print "obj.%s = %s" % (attr, getattr(obj, attr))

	res = []
		
        th = linha.findAll('th')

        del th[0]
        i = 0
        for t in th:
            r = t.find('a')
#            dump(r)
#            print r.text + '\n'
            if r.text.startswith('EP'):
                res.append(i)
            i += 1
        return res

    def getStudentsGrades(self, table):
        rows = table.findAll('tr')
	del rows[0]
		
	indexEps = self.getCelulas(rows[0])

        del rows[0]
        del rows[-1]
	res = []
	for row in rows:
            x = []
            name = row.find('th').findAll('a')[1].contents[0]
            name = strip_accents(name)
            
            cols = row.findAll('td')

            grades = []
            for e in indexEps:
                s = cols[e].find('span').contents[0].replace(',', '.')
                if s != '-' and s != '0.00':
                    grades.append(float(s))

            x.append(name)
            x.append(grades)
            res.append(x)
        return res
