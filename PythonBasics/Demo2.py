
values = [1, 2, "rahul", 4, 5]
#List is data type that allows multiple values and can be different data types

print(values[0]) #1 

print(values[2]) #rahul

print(values[-1]) #5

print(values[1:3]) # [2, 'rahul'] - Slicing the list

# Adding an element to the list
values.append(3,"shetty")
print(values)

values.append("shetty")
print(values)

# Updated list
values[0] = 10

print(values)  # [10, 2, 'rahul', 4, 5, 3, 'shetty']

# Removing an element from the list
values.remove("shetty")
print(values)  # [10, 2, 'rahul', 4, 5, 3]

#Tuple
# Tuple is similar to list but immutable (cannot be changed after creation)
my_tuple = (1, 2, "rahul", 4, 5)
print(my_tuple[2])  # rahul

#Dicitionary
# Dictionary is a collection of key-value pairs
my_dict = {
    "name": "rahul",
    "age": 30,
    "city": "Mumbai"
}

print(my_dict["name"])  # rahul
print(my_dict["age"])   # 30
print(my_dict["city"])  # Mumbai

# Adding a new key-value pair
my_dict["country"] = "India"
print(my_dict)  # {'name': 'rahul', 'age': 30, 'city': 'Mumbai', 'country': 'India'}

# Removing a key-value pair
del my_dict["age"]
print(my_dict)  # {'name': 'rahul', 'city': 'Mumbai', 'country': 'India'}

##########################################################################################################
# If statements #else statements

# If statements are used to execute a block of code based on a condition

greeting = "Good Morning"

if greeting == "Morning":
    print("Good Morning to you too!")
else:
    print("Hello!")
print("if else condition code is completed")
# This will print "Hello!" because the condition is not met


#####################################################################################
#loops
# Loops are used to iterate over a sequence (like a list or a string)

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)  # This will print each element in the list

# sum of First Natural numbers 1+2+3+4+5 = 15

for j in range(1, 6):  # range(start, stop) generates numbers from start to stop-1
    print(j)  # This will print numbers from 1 to 5







