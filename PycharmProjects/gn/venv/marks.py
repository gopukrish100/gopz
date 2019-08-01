mark1=int(input("enter the mark of subject 1"))
mark2=int(input("enter the mark of subject 2"))
mark3=int(input("enter the mark of subject 3"))
total=mark1+mark2+mark3
if(total>140):
    print("A+")
elif(total>130) & (total<=140):
    print("A")
elif(total>120) & (total<=130):
    print("B+")
else:
    print("failed")
if(mark1>=mark2)&(mark1>=mark3):
    print(mark1)
elif(mark2>=mark1)&(mark2>=mark3):
    print(mark2)
else:
    print(mark3)
