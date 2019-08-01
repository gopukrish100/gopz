class Student:
    schoolname='luminar'
    def __init__(self,name,rol):
        self.name=name
        self.rol=rol
    def display(self):
        print('name=',self.name)
        print('roll no',self.rol)
    def __str__(self):
        return self.name+str(self.rol)

obj=Student('anj',12)
obj.display()

print(obj)