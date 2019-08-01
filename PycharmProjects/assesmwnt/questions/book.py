class Book:
    def __init__(self,pages):
        self.pgs=pages
    def __add__(self, other,):
        bk=Book(self.pgs+other.pgs)
        return bk
    def __str__(self):
        return str(self.pgs)
    def __sub__(self, other):
        bk=Book(self.pgs-other.pgs)
        return bk
    def __mul__(self, other):
        return self.pgs*other.pgs
    def __truediv__(self, other):
        return self.pgs/other.pgs

b1=Book(82)
b2=Book(45)
b3=Book(35)
print(b1+b2+b3)
print(b1-b2-b3)
print(b1*b2)
print(b1/b2)
