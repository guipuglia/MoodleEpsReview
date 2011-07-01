import Login
import Parser
import Student


if __name__ == '__main__':
	x = Login.Login('7259186', 'senha1')
	x.connect('username', 'password')
	#p = Parser(x.open('http://paca.ime.usp.br/mod/assignment/submissions.php?id=12397'))
	p = Parser.Parser(x.open('http://paca.ime.usp.br/mod/assignment/submissions.php?id=12397&tsort=firstname'))
	table = p.clean()
	st = p.getStudents(table)
	i = 1
	for s in st:
		print "%d :: %s" % (i, s)
		print '---------------'
		i += 1

