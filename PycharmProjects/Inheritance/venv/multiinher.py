class One:
    def m1(self):
        print('inside class one')
class Two(One):
    def m1(self):
        print('inside class two')
class Three(Two,One):
    def m3(self):
        print('inside class three')

obj=Three()
obj.m3()
obj.m1()