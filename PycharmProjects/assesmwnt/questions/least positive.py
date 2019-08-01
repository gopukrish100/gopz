lst=[]
n=int(input('enter no of elements'))
for i in range(0,n):
    el=int(input('enter element'))
    lst.append(el)
lst.sort()
for i in lst:
    if(i>=0):
        print(i)
        break
    

