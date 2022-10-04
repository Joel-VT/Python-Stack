from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()

while( player_1.health > 0 and computer.health > 0):
    response =""
    while (response not == "1" and not response not == "2"):
        print("You are the Barbarian, will you \n 1)Attack \n 2)Defend or \n 3)Heal")
        response = input(">>>")
        if response == "1":
            player_1.attack(computer)
        elif response == "2":
            player_1.heal()
        else:
            print("please select a valid option")
    computer_action = random.randint(1,3)
    if computer_action == 1:
        computer.attack(player_1)
    if computer_action == 2:
        enemy.use_totem()
    if enemy_action == 3:
        enemy.heal()

if enemy.health < 0:
    print(f"You have defeated {enemy.name}")
else: print(f"The mighty barbarian has fallen")