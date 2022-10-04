import random
from pet import Pet
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        print(f"{self.first_name} takes {self.pet.name} for a walk")
        self.pet.play()
        return self

    def feed(self):
        random_treat = random.randint(0,len(self.treats))
        print(f"{self.first_name} feeds {self.pet.name} {self.treats[random_treat]} and {self.pet_food}")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"{self.first_name} bathes {self.pet.name}")
        self.pet.noise()
        return self



ninja_man = Ninja("Joel", "VT", ["Bacon Bits","Tuna Bits"], "Pizza", Pet("Mr. Nibbles", "Cat", ["Purr", "Sit on tail"]))

ninja_man.walk().feed().bathe()
