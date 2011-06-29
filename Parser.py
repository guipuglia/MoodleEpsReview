import BeautifulSoup
import unicodedata
import Student

def strip_accents(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

class Parser:
    def __init__(self, document):
        self.document = document
        self.soup = BeautifulSoup.BeautifulSoup(self.document)

    def clean(self):
        table = self.soup.find('table', {'class':'flexible submissions'})
        return table

    def getStudents(self, table):
        rows = table.findAll('tr')

        del rows[0]

        res = []

        for row in rows:
            tdName = row.find('td', {'class': 'cell c1 fullname'})
            name = strip_accents(tdName.find('a').contents[0])
#            print strip_accents(name) 
            tdFile = row.find('td', {'class': 'cell c4 timemodified'})
            if tdFile.find('a') is not None:
                fileLink = tdFile.find('a')['href']
#                print fileLink
            else:
                fileLink = ''
#                print "Nao tem arquivo"
            tdStatus = row.find('td', {'class': 'cell c6 status'})
            statusLink = tdStatus.find('a')['href']
#            print statusLink
#            print "---------------------"

            if fileLink != '':
                res.append(Student.Student(name, fileLink, statusLink))

        return res
