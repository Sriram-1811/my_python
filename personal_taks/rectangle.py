class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def area(self):
        return self.length*self.breadth
    
r1= Rectangle(10,20)
print("area of the rectangle is:",r1.area())
print("perimeter of the rectangle is:",r1.perimeter())
