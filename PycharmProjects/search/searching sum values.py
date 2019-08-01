def search(lst,el):
    for i in lst:
        for j in lst:
            if(i+j==el):
                print(i,j)
            break

lst=[]
s=int(input('eneter the size o list'))
for i in range(0,s):
    e=int(input('enter the element'))
    lst.append(e)
el=int(input('eneter the search element'))
search(lst,el)
