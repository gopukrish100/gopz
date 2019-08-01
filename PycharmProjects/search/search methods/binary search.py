def binarysearch(lst,elem):

    lst.sort()
    low=0
    upp=len(lst)
    mid=(low+upp)//2

    while(low<upp):
        if(elem<lst[mid]):
            upp=mid-1
        elif(elem==lst[mid]):

            print('element found')
            break
        elif(elem>lst[mid]):
            low=mid+1
        mid=(low+upp)//2
lst=[]
no=int(input('eneter the size of list'))
for i in range(0,no):
    el=int(input('enter the element'))
    lst.append(el)
elem=int(input('eneter the search element'))
binarysearch(lst,el)
