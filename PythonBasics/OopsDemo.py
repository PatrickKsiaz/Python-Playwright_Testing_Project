#Classess unsing defined blueprint or prototype
#sum, multiplication,addition, constant

#methods, class variables, instance variables, constructor
# self keyword is mandatory for calling variable names into method
# constuctor name should be __init__
# new keywword is not required when you crete object




class Calculator:
    num = 100   # class var
    
    #default constructor
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("Constructor is called")
    

    def getData(self):
        print("I am now executing as method in class")
    
    def Summation(self):
        return self.firstNumber + self.secondNumber
    
    def Multiplication(self):
        return self.firstNumber * self.secondNumber
    
    def Division(self):
        return self.firstNumber / self.secondNumber
    
    def Subtraction(self):
        return self.firstNumber - self.secondNumber
    


obj = Calculator(2,3)  # Syntax to create an object in Python
obj.getData()  # Calling the method of the class
print(obj.Summation())  # Accessing the class variable

obj1 = Calculator(4,5)
obj1.getData
print(obj1.Summation())  # Accessing the class variable






