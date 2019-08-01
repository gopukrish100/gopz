# class person:
#     def welcome(self):
#
#         print('welcome user')
# obj=person()
# print(type(obj))
#
# obj.welcome()

# class student:
#     def displayvalues(self,name,roll,college):
#         self.roll=roll
#         self.name=name
#         self.college=college
#         print('name=',self.name)
#         print('roll=',self.roll)
#         print('college=',self.college)
# obj=student()
# obj.displayvalues('gopu',36,'luminar')
# obj1=student()
# obj2=student()
# obj1.displayvalues('sonu',40,'cemp')
# obj2.displayvalues('vishnu',44,"cemp")


# class Student:
#     def setvalues(self,rol,name,clg):
#         self.rol=rol
#         self.name=name
#         self.clg=clg
#     def markdetails(self,mark):
#         self.mark=mark
#
#
#     def Display(self):
#         print('roll no=',self.rol)
#         print('name=',self.name)
#         print('college=',self.clg)
#         print('mark=',self.mark)
# obj=Student()
# obj.setvalues(36,"gopu",'luminar')
# obj.markdetails(70)
# obj.Display()


class Bank:
    def setvalues(self,acno):
        self.min=3000
        self.bnknm='SBI'
        self.acno=acno
    def deposit(self,dep):
        self.dep=dep
        self.bal=self.min+self.dep
        print('deposit amt=',self.dep)
        print('new balance=',self.bal)
    def withdrawal(self,remt):


        self.remt=remt
        self.bal=self.bal-self.remt
        print('remitting amt=',self.remt)
        print('balance amt=',self.bal)

    def bal_enq(self):
        print('acc no=',self.acno)
        print('bankname=',self.bnknm)

        print('balance=',self.bal)
obj=Bank()
obj.setvalues(100)
obj.deposit(15000)
obj.withdrawal(5000)
obj.bal_enq()