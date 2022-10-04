# Countdown
def countdown(num):
    list = []
    for i in range(num,-1,-1):
        list.append(i)
    return list

print(countdown(5))

# Print and return
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))

# First and Return
def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))

# Values Greater than Second
def values_greater_than_second(list):
    if len(list) >= 2:
        temp_list = []
        for val in list:
            if val > list[1]:
                temp_list.append(val)
        print(len(temp_list))
        return temp_list
    
    else:
        return False

print(values_greater_than_second([6]))

# This Length, That Value
def length_and_value(size,value):
    list = []
    for i in range(size):
        list.append(value)
    return list

print(length_and_value(4,5))