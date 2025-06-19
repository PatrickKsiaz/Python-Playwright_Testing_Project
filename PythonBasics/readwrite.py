file = open('test.txt')
#Read all the contents of the file

#Read n number of characters by passing parameters
#print(file.read(5))
#read one single line at a time


print(file.readline())
print(file.readline())



#Print line by line using readline method
#line = file.readline()
#while line != "":
#    print(line)
#    line = file.readline()

for line in file.readlines():
    print(line)
#Print all the lines at once
    




file.close()

