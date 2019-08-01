def Uper(lst):
    lst2=[]
    for i in lst:
        lst2.append(i.upper())
    print(lst2)
lst=[]
n=int(input('eneter no of elements'))
for i in range(0,n):
    el=int(input('eneter element'))
    lst.append(el)
Uper(lst)

