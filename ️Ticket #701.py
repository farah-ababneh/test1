class Student:
    def _init_(self,name:str,student_Id,grades:int):
        self.name = name
        self.student_Id = student_Id
        self.grades = grades
def GPA(self):
    return sum(self.grades)/len(self.grades)