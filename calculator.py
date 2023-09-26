#Calculation functions

def add (x,y):
    return x+y

def subtract (x,y):
    return x-y

def multiply (x,y):
    return x*y

def divide (x,y):
    if y==0:                #zero nk tu ny yin division ma phyit loh d lo htae ya tr
        return "Cannot divided by zero!"
    return x/y

#Main calculator loop
while True:
    print("Operations")
    print("Enter 'add' for addition")
    print("Enter 'sub' for subtract")
    print("Enter 'divide' for division")
    print("Enter 'multiply' for multiplication")
    print("Enter 'quit' to quit the program")
    user_input= input(": ")
    if user_input=="quit":                  #break so tr ka program ko stop foh py tk command
        break
    elif user_input in ["add", "sub", "divide", "multiply"]:
        number1 = float(input("Enter your first number= "))
        number2 = float(input("Enter your second number= "))

        if user_input=="add":
            print("Result:", add(number1,number2))
        elif user_input=="sub":
            print("Result:", subtract(number1,number2))
        elif user_input=="divide":
            print("Result:", divide(number1,number2))
        elif user_input=="multiply":
            print("Result:", multiply(number1,number2))
        else:
            print("Invalid input. Please enter a valid option.")








