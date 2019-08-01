class Student:
    school='luminar Technolab'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.3)/3
    @classmethod
    def info(cls):
        cls.school='techno lab'
        print(cls.school)
    @staticmethod
    def staticMeth():
        print('inside static method')
s1=Student(50,45,40)
print()