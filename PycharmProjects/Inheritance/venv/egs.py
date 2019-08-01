class One:
    def m1(self):
        print('im inside parent m1 method')



class Two(One):
    def m2(self):
        print('im inside class two')

obj=Two()
obj.m2()
obj.m1()


