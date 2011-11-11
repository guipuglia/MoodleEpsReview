# -*- coding: utf-8 -*-
import Login
import Parser
import Student

def defineGrades(login):
	p = Parser.Parser(login.open('http://paca.ime.usp.br/grade/report/grader/index.php?id=491&perpage=100&page=0&sortitemid=firstname'))
	table = p.clean('table','id', 'user-grades')
	listSt = p.getStudentsGrades(table)
	
	pp = Parser.Parser(login.open('http://paca.ime.usp.br/mod/assignment/submissions.php?id=12535&tsort=firstname'))
	table = pp.clean('table','class', 'flexible submissions')
        print table

	sst = pp.getStudents(table)
	for s in sst:
            for e in listSt:
                if s.name == e[0]:
#                    print s
#                    print e[1]
#                    print '-------'
                    comments = ''
                    grades = e[1]
                    final = 0
                    if len(grades) < 2:
                        final = 0
                        comments = 'Entregou menos que 2 eps.'
                    if len(grades) == 2:
                        final = 20
                        comments = 'Entregou 2 eps. (REPROVADO)'
                    elif len(grades) == 3:
                        final = 30
                        comments = 'Entregou 3 eps. (RECUPERAÇÃO)'
                    else:
                        grades.sort()
                        if len(grades) == 5:
                            del grades[0]
                        for g in grades:
                            final += float(g)/4
                    ans = int(final)
                    if final - float(ans) >= 0.5:
                        ans += 1
#                    print str(final) + '   ' + str(ans)
                    s.reviewEntregou(login, 'http://paca.ime.usp.br/mod/assignment/submissions.php', ans, comments)
                    print 'publicou'
                    break




		

def correctionOfEpMode(login):
	#p = Parser(login.open('http://paca.ime.usp.br/mod/assignment/submissions.php?id=12397'))
	p = Parser.Parser(login.open('http://paca.ime.usp.br/mod/assignment/submissions.php?id=12435&tsort=firstname'))
	table = p.clean('table','class', 'flexible submissions')
	st = p.getStudents(table)
	for s in st:
		if s.fileLink == '':
			s.reviewNaoEntregou(login, 'http://paca.ime.usp.br/mod/assignment/submissions.php')
			print str(s) + '\nNão entregou'
		else:
			print s
			print "Criando diretório:"
#			s.createDir('/home/gui/Dropbox/Mestrado/2011/mac323/EPSub/Eps/')
#			print "Baixando arquivo:"
#			s.downloadFile(login, '/home/gui/Dropbox/Mestrado/2011/mac323/EPSub/Eps/')
#			s.copyFile( '/home/gui/Dropbox/Mestrado/2011/mac323/EPSub/template.txt',
#						'/home/gui/Dropbox/Mestrado/2011/mac323/EPSub/Eps/', 'comentario.txt')

			print "Parser Nota:"
			nota, comments = p.getResults('/home/gui/Dropbox/Mestrado/2011/mac323/EPSub/Eps/' + s.name.replace(' ', '_') +  '/comentario.txt')
			print str(nota) + ' / 100'
			print "Review"
			s.reviewEntregou(login, 'http://paca.ime.usp.br/mod/assignment/submissions.php', nota, comments.replace('\n', '<p>\n'))
		print '---------------'	

if __name__ == '__main__':
#	login = Login.Login('7259186', raw_input('Senha: '))
	login = Login.Login('7259186', '')
	login.connect('username', 'password')
#	correctionOfEpMode(login)
	defineGrades(login)

