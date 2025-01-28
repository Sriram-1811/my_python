class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def start(self):
        print("The",self.brand,self.model,'is starting')

c1=Car("porsche","Cayenne Coupe",2025)
c1.start()