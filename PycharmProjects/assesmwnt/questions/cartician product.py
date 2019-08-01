# lst=[]
# lst2=[]
# n=int(input('eneter the no of elements in lst'))
# for i in range(0,n):
#     e=int(input('eneter element'))
#     lst.append(e)
# m=int(input('enter no of  element in lst2'))
# for i in range(0,m):
#     r=int(input('eneter element'))
#     lst2.append(r)
# lst3=[]
# def Cart():
#     for i in lst:
#         for j in lst2:
#             tup=(i,j)
#         lst3.append(tup)
#     print(lst3)
# Cart()

#or

A=[1,2,3]
B=[3,4,5]
cart=[(a,b) for a in A for b in B]
print(cart)

