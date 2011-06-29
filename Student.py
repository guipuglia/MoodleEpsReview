
class Student:
    def __init__(self, name, fileLink, gradeLink):
        self.name = name
        self.fileLink = fileLink
        self.gradeLink = gradeLink

    def __str__(self):
        s = "%s\n%s\n%s" % (self.name, self.fileLink, self.gradeLink)
        return s
