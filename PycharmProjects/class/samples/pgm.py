class Student:
    schoolname='Luminar Tech'
    def setvalues(self,rol,name,mark1,mark2):
        self.rol=rol
        self.name=name
        self.mk1=mark1
        self.mk2=mark2
    def displayvalues(self):
        print('student name',self.name)
        print('clg name',Student.schoolname)
        print('mark1',self.mk1)
    def average(self):
        self.avg=(self.mk1+self.mk2)/2
        print('average mark',self.avg)
    def sort(self):



obj1=Student()
obj1.setvalues(1001,"anj",120,130)
obj1.displayvalues()
obj2=Student()
obj2.setvalues(1002,"ann",130,140)
obj2.average()
obj2.displayvalues()
obj3=Student()
obj3.setvalues(1003,'gopu',1300,1400)
obj3.average()
obj3.displayvalues()
