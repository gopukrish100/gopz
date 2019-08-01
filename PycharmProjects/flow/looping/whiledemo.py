i=9
while(i>0):
    print(i)
    i-=1
number=int(input("enter a number"))
res=0
while(number!=0):
    digit=number%10
    res=res*10+digit
    number=number//10
    print(res)
