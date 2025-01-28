"""Implement a Zoo class to manage animals.
 Use a dictionary to store the number of each type of animal.
 Add methods to add animals, remove animals, and get a count of all animals."""
class Zoo:
    def __init__(self):
        self.animals={}

    def add_animals(self,animal_name):
        if animal_name in self.animals:
            self.animals[animal_name]+=1
        else:
            self.animals[animal_name]=1
            print(animal_name,"was successfully added into zoo")

    def remove_animals(self,animal_name):
        if animal_name in self.animals:
            self.animals[animal_name]-=1
            if self.animals[animal_name]==0:
                del self.animals[animal_name]
            print(animal_name,"was successfully removed from zoo")
        else:
            print("animal named",animal_name,"was not found in the zoo")
    
    def list_animals(self):
        if self.animals:
            for animal, count in self.animals.items():
                print(animal,":",count)
        else:
            print("zoo is empty")

    def get_animal_count(self):
        total_count=sum(self.animals.values())
        print("Total number of animals in the zoo:", total_count)
        return print(total_count)

z1=Zoo()

z1.add_animals("monkey")
z1.add_animals("tiger")
z1.add_animals("kangaroo")
z1.add_animals("kiwi")
z1.add_animals("monkey")
z1.add_animals("tiger")
z1.add_animals("kangaroo")
z1.add_animals("kiwi")
z1.add_animals("monkey")
z1.add_animals("tiger")
z1.add_animals("kangaroo")
z1.add_animals("kiwi")
z1.add_animals("Lion")
z1.add_animals("Lion")
z1.remove_animals("kangaroo")
z1.get_animal_count()
print(z1.animals)
z1.list_animals()