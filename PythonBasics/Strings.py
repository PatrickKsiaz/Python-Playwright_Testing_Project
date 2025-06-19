str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShettyAcademy"


print(str[1])   #a

print(str[0:5]) # if you want substirng in Python

print(str + str1) # Concatenation of two strings

print(str3 in str) # Check if str3 is a substring of str


var = str.split(".")  # Split the string at the dot
print(var)  # This will print ['RahulShettyAcademy', 'com']
print(var[0])  # This will print 'RahulShettyAcademy'

str4 = "Great"
print(str4.strip())  # This will remove any leading or trailing whitespace, but since there is none, it will print 'Great'
print(str4.lstrip())
print(str4.rstrip())  # This will also print 'Great' since there is no trailing whitespace









