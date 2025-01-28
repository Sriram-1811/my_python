class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print('the average marks scored by',self.name,'is',sum/(len(self.marks)))

s1=Student('sharma',[10,15,7])

s1.avg()
