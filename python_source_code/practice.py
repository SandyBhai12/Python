class Circle:
    def __init__(self,r):
        self.r=r
        self.pi=3.142
    def area(self):
        self.area=self.pi*self.r*self.r
        print("area of the circle is = :",self.area)
    
    def perimeter(self):
        self.peri=2*self.pi*self.r
        print("perimeter of the circle is = :",self.peri)

c=Circle(21)
c.area()
c.perimeter()
