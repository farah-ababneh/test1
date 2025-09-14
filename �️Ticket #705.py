class Stu: pass
def _init_(self,grades):
    self.grades=grades
def gpa(self):
    return sum(self.grades)/len(self.grades)