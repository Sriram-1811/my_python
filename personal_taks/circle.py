import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    @classmethod
    def from_diameter(cls, diameter):
        radius=diameter/2
        return cls(radius)
    
    def area(self):
        area=math.pi*(self.radius**2)
        print("radius of the circle is:", area)

c1=Circle.from_diameter(10)

c1.area()
