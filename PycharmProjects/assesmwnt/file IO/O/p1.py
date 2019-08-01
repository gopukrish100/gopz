# f=open('employee')
# lst=[]
# for i in f:
#     lst.append(i[:-1].split(','))
# lst2=sorted(lst,key=lambda x:x[2],reverse= True)
# print(lst)
# for i in lst2:
#     if (int(i[2])>=19000):
#         print(i[1])


class Employee:
    def __init__(self,eid,ename,esal,edesig):
        self.eid=eid
        self.ename=ename
        self.esal=esal
        self.edesig=edesig
    def __str__(self):
        return self.ename+str(self.eid)+'\n'
elist=[]
lst=[]
f=open('employee')
for i in f:
    lst=(i[:-1].split(','))
    elist.append(Employee(lst[0],lst[1],lst[2],lst[3]))
# for i in elist:
#     print(i)
srt=sorted(elist,key=lambda x:x.ename,reverse=False)
for i in srt:
    print(i)