# list1=[23,25,63,66,77,26,75,45,54,84,48]
# n=len(list1)
# for i in range (0,n):
#     if(list1[i]%2==0):
#         print(list1[i])
#         i+=1
#     else:
#         continue
#
# list1.append(5)
# print(list1)

# lst=[25,30,35,40,45,50]
# print(lst)
# odd=[]
# even=[]
# for i in lst:
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(odd)
# print(even)

# lst=[10,20,22,30,33,40,44,50,55]
# print(len(lst))
# print(lst.count(55))
# print(max(lst))
# print(min(lst))

n=int(input("enter the number of elements"))
lst=[]
for i in range(0,n):
    e=int(input('eneter the next object'))
    lst.append(e)

print(lst)
lst.sort()
print()
for j in lst:
    if(lst[j]+1!=lst[j+]):

