lst=[('ajay',25000),('sijo',20000),('danie',40000),('vinu',18000)]
# sal=20000
# for i in lst:
#     if(i[1]>=sal):
#         print(i[0])
#


emp=[name for(name,sal) in lst if sal>20000]
print(emp)
