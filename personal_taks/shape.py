from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self,length):
        self.length=length

    def area(self):
        area=self.length**2
        print("area of the square is",area)
    
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        area= (1/2)*self.base*self.height
        print("area of the triangle is",area)

s1=Square(4)
s1.area()

s2=Triangle(5,10)
s2.area()