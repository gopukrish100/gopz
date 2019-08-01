# r=int(input("input range"))
# n=0
# while(n<=r):
#     print(n)
#     n+=1

# l=int(input("enter the lower range"))
# u=int(input("enter the upper range"))
# while(l<=u):
#     print(l)
#     l+=1

# #
# i=int(input("enter the lower limit"))
# r=int(input("enter the upper limit"))
# if(i%2==0)& (i<=r):
#     print(i)
#     i+=2
# else:
#     i+=1
#
# # num=int(input("enter input num"))
# res=0
# while(num!=0):
#     digit=num%10
#     res=res*10+digit
#     num=num//10
# # print(res)
# num=int(input("enter the number "))
# for i in range(0,num,2):
#     print(j,"*",i,"=",j*i)
# def add():
#     num=int(input("nol"))
#     num2=int(input("nol"))
#     res=num+num2
#     print("res=",res)
#
#     add()

def prime(no):
    flg=0
    for i in range(2,no):
        if(no%i==0):

            flg+=1
    else:
        pass
    if(flag==0):

        return True
    else:
        return False

value=prime (5)
print(value)