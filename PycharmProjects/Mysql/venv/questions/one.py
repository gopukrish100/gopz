class Circle:
    def __init__(self,rad):
        self.rad=rad
    def perimeter(self):
        peri=2*3.14*self.rad
        print('perimeter=',peri)
    def area(self):
        area=3.14*(self.rad**2)
        print('area=',area)
n=int(input('enter radius'))
obj=Circle(n)
obj.perimeter()
obj.area()