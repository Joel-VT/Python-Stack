num1 = 42  # -variable declaration -Numbers
num2 = 2.3 # -variable declaration -Numbers -Floating point value
boolean = True # -variable declaration -Boolean
string = 'Hello World' # -variable declaration -Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # -List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # -Dictionary -initialize
fruit = ('blueberry', 'strawberry', 'banana') # -Tuples -inititalize
print(type(fruit)) # -log statement -prints tuple fruit
print(pizza_toppings[1]) # -log statement -prints Sausage
pizza_toppings.append('Mushrooms') # -add value
print(person['name']) # -access name value in dictionary person
person['name'] = 'George' # -change value
person['eye_color'] = 'blue' # -add value
print(fruit[2]) # -access value in tuple

if num1 > 45: # -if
    print("It's greater") # - body of if
else:   # -else
    print("It's lower") # -body of else

if len(string) < 5: # -if
    print("It's a short word!") # - body of if
elif len(string) > 15:  # -else if
    print("It's a long word!") # - body of else if
else:   # -else
    print("Just right!")    # -body of else

for x in range(5): # -for loop -start
    print(x) # -body of loop
for x in range(2,5):    # -for loop -start
    print(x)    # -body of loop
for x in range(2,10,3): # -for loop -start
    print(x)    # -body of loop
x = 0   # -variable declaration -Numbers
while(x < 5):   # -while loop -start
    print(x) # -body of while loop
    x += 1  # -increment

pizza_toppings.pop() # -delete value
pizza_toppings.pop(1) # -delete value at index 1

print(person) # -log statement
person.pop('eye_color') # -delete value
print(person)   # -log statement

for topping in pizza_toppings:  # -for loop -start
    if topping == 'Pepperoni':  # -if
        continue    # -continue
    print('After 1st if statement') # -log statement
    if topping == 'Olives': # -if
        break   # -break

def print_hello_ten_times():    # -function
    for num in range(10):   # -for loop -start
        print('Hello')  # -log statement

print_hello_ten_times() # -log statement

def print_hello_x_times(x): # -function -parameter
    for num in range(x): # -for loop -start
        print('Hello')  # -log statement

print_hello_x_times(4) # -function -argument

def print_hello_x_or_ten_times(x = 10): # -function -parameter
    for num in range(x):    # -for loop -start
        print('Hello')  # -log statement

print_hello_x_or_ten_times()    # -function
print_hello_x_or_ten_times(4)   # -function -argument


"""
Bonus section
"""

# print(num3)  - NameError: name <variable name> is not defined
# num3 = 72  --variable declaration -Numbers
# fruit[0] = 'cranberry'   - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])    - KeyError: 'favorite_team'
# print(pizza_toppings[7])  - IndexError: list index out of range
#   print(boolean)  - IndentationError: unexpected indent
# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  - AttributeError: 'tuple' object has no attribute 'pop'