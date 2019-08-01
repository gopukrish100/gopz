# def isEven(num):
#
#     if(num%2==0):
#         return True
#     else:
#         return False
# lst=[10,20,25,35,44,55,66,77]
# evnlst=list(filter(isEven,lst))
# print(evnlst)



lst=['sachin','rahul','sehwag','yuvi','kohli','hardik']
names=list(map(lambda str:str.upper(),lst))
print(names)
fname=list(filter(lambda x:x.startwith('S'),names))
