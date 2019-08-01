
number1=int(input("enter mark1"))
number2=int(input("enter mark2"))
sum=number1+number2
if(sum>90):
    print("A+")
elif((sum>80) & (sum <= 90)):
    print("A")
elif((sum>70) & (sum <= 80)):
    print("B+")
else:
    print("just passed")