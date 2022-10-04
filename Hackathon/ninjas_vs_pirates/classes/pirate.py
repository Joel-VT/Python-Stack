import random
class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

    def pocket_sand(self, ninja):
        ninja.speed -= 4
        if ninja.speed < 0:
            ninja.speed = 0
        print(f"{ninja.name}'s speed is reduced to {ninja.speed}")

    def drink_beer(self):
        self.strength += 2
        self.health -= 2

    def throw_glass(self, ninja):
        hit_amount = random.randint(0,15)
        ninja.health
