def lcm():
    a=2
    n1=int(input('eneter the first no'))
    n2=int(input('enter the second no'))
    if(n1>n2):
        x=n2
        n2=n1
        n1=x
        for i in range(a,n2):
            if(n1%a==0 and n2%a==0):
                print('lcm=',a)
                break
            elif():
                a+=1
                return a
lcm()