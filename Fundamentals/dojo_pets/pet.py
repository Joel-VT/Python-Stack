class Pet:
    def __init__(self, name, pet_type, tricks):
        self.name = name
        self.pet_type = pet_type
        self.tricks = tricks
        self.health = 10
        self.energy = 10

    def sleep(self):
        print(f"{self.name} is sleeping now")
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10
    
    def play(self):
        self.health += 5
    
    def noise(self):
        if self.pet_type.lower() == "cat":
            print("Meow")
        if self.pet_type.lower() == "dog":
            print("Woof")