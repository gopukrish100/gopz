def fibonacci(n):
    ini=0
    sec=1
    print(ini)
    print(sec)
    for i in range(0,n-2):
        nex=ini+sec
        print(nex)
        ini=sec
        sec=nex
n=int(input('eneter length'))
fibonacci(n)