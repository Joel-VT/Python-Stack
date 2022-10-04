class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"First Name: {self.first_name} \nLast Name: {self.last_name} \nEmail: {self.email} \nAge: {self.age} \nRewards Member: {self.is_rewards_member} \nGold Card Points: {self.gold_card_points}")
        return self
    
    def enroll(self):
        if self.is_rewards_member != True:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
        else: 
            print("User already a member.")
            return False
    
    def spend_points(self, amount):
        if self.gold_card_points - amount >= 0:
            self.gold_card_points -= amount
            print(f"Successfully Spent {amount} points")
        else:
            print("Insufficient Points")
        return self


new_user = User("Joel", "Varghese", "joelvarghese90@gmail.com", 24)
print(new_user.display_info().enroll())


new_user2 = User("Jacob", "Bryant", "jacobbryant@gmail.com", 20)

new_user3 = User("John", "Thomas", "johnt@gmail.com", 25)

new_user.spend_points(50)

print(new_user2.enroll())
new_user2.spend_points(80).display_info()


print(new_user.display_info().enroll())
new_user3.display_info().spend_points(40)