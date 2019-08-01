class Person:
    def setPerson(self,age,name,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def displayPerson(self):
        print(self.name+ str(self.age)+ self.gender)
class Student(Person):
    school='Luminar'
    def __init__(self,mk1,mk2):
        self.mk1=mk1
        self.mk2=mk2
    def calc(self):
        self.total=self.mk1+self.mk2
        print('total=',self.total)
        print('college',Student.school)
class Employee(Person):
    def details(self,idno,sal):
        self.id=idno
        self.sal=sal
        print('Id No.=',self.id)
        print('salary=',self.sal)

st=Student(50,45)
st.setPerson(25,'anj','m')
st.displayPerson()
st.calc()

em=Employee()
em.setPerson(25,'gopu','male')
em.displayPerson()