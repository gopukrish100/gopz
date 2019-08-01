# f=open('text.txt',"r")
# g=open('txt2','a')
# g.write(f.read())

# fin=open('text.txt')
# f=open('txt2','a')
# for val in fin:
#     f.write(val)

f=open('text.txt')
g=open('txt2')
h=open('txt3','a')
lst=[]
for i in f:
    lst.append(i[:-1])
print(lst)
lst2=[]
for i in g:
    lst2.append(i[:-1])
print(lst2)

for val in lst:
    for j in lst2:
        h.write(val+' '+j+'\n')

        break
