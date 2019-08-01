def linearsearch(lst,element):
    flag=0
    print(lst,element)
    for i in lst:
        if(i==element):
            flag+=1
            break
        else:
            pass
    if(flag==0):
            return False
    else:
            return True


lst=[]
lim=int(input('eneter how mwny elements u wnt to add'))

for i in range(0,lim):

    val=int(input('eneter value to insert into list'))
    lst.append(val)

element=int(input('eneter the element to search'))
print(linearsearch(lst,element))
