class Employee:
    def __init__(self,nm,id,sal):
        self.nm=nm
        self.id=id
        self.sal=sal
    def __str__(self):
        return str(self.nm)



obj1=Employee("Gopu",100,29000)
obj2=Employee("Bince",101,39000)
obj3=Employee("Justin",102,37000)
lst=[]
lst.append(obj1)
lst.append(obj2)
lst.append(obj3)
for i in lst:
    print(i)
slist=sorted(lst,key=lambda emp:emp.sal,reverse=False)
for f in slist:
    print(f)