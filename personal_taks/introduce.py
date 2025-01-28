class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print("Hi, my name is ",self.name,"age is ",self.age)

p1=Person("sriram",22)

p1.introduce()
