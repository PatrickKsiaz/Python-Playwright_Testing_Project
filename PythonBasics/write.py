file = open('test.txt')

file.close()

#Read the file and store all the lines in list
#Reverse the list
#Write the list back to the file


with open ('test.txt', 'r') as reader:
    content = reader.readlines()  # Read all lines into a list
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


