
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






