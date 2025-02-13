"""Implement a `Polynomial` class to represent a polynomial (e.g., 3x^2 + 2x + 1).
    Add methods to evaluate the polynomial for a given value of `x` and to perform addition and subtraction with another polynomial."""

class Polynomial:
    def __init__(self,terms=None):
        if terms is None:
            self.terms=[]
        else:
            self.terms=terms
    
    def __str__(self):
        if not self.terms:
            return "0"
        
        poly_expression=[]
        for coef,exp in self.terms:
            poly_expression.append(str(coef)+"*(x**"+str(exp)+")")

        return "+".join(poly_expression)
    
    def evaluate(self,x):
        result=0
        for coef,exp in self.terms:
            result+= coef*(x**exp)
        return result

poly=Polynomial([(3,2),(2,1),(1,0)])
print(poly)
intval=int(input("enter the value of x:"))
print(poly.evaluate(intval))