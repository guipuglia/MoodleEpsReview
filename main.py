# -*- coding: utf-8 -*-
import Login
import Parser
import Student

if __name__ == '__main__':
	login = Login.Login('7259186', raw_input('Senha: '))
	
	login.connect('username', 'password')
	#p = Parser(login.open('http://paca.ime.usp.br/mod/assignment/submissions.php?id=12397'))
	p = Parser.Parser(login.open('http://paca.ime.usp.br/mod/assignment/submissions.php?id=12397&tsort=firstname'))
	table = p.clean()
	st = p.getStudents(table)
	for s in st:
		if s.fileLink == '':
			s.reviewNaoEntregou(login, 'http://paca.ime.usp.br/mod/assignment/submissions.php')
		else:
			print s
			print "Criando diretório:"
			s.createDir('/home/gui/Dropbox/Mestrado/2011/mac323/EP4/Eps/')
			print "Baixando arquivo:"
			s.downloadFile(login, '/home/gui/Dropbox/Mestrado/2011/mac323/EP4/Eps/')
			print '---------------'
