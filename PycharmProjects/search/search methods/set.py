days= {'monday', 'tuesday','wednesday','thursday','friday'}
print(days)
print(type(days))
print(('looping through the search elements'))
for i in days:
    print(i)

days.add('saturday')

print(days)

days.pop()
print(days)

d={1,2,3,5,6,7}
a={3,4,6,8}
print(d|a)
print(a&d)

college={'arun','vishnu','sonu','kiran'}
failed={'arun','vishnu'}
passed=college-failed
print(passed)