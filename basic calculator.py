import math
def greet():
    print("****** WELCOME TO MY CALCULATOR PROGRAM ******")

def numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def mul(x,y):
        return x*y
    def div(x,y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

    return add(num1, num2), sub(num1, num2), mul(num1, num2), div(num1, num2)

def print_results(addition=None, subtraction=None, multiplication=None, division=None):
    if addition is not None:
        print(f"The sum is {addition}")
    if subtraction is not None:
        print(f"The difference is {subtraction}")
    if multiplication is not None:
        print(f"The product is {multiplication}")
    if division is not None:
        print(f"The quotient is {division}")

def user_input():
    addition,subtraction,multiplication,division = numbers()
    user_in = input('''Which operation do you want to perform?
                    1. Addition
                    2. Subtraction
                    3. Multiplication
                    4. Division
                    ''').strip()
    if user_in == '1':
        print_results(addition=addition)
    elif user_in == '2': 
        print_results(subtraction=subtraction)
    elif user_in == '3':
        print_results(multiplication=multiplication)
    elif user_in == '4':
        print_results(division=division)
    else:
        print("Please enter a valid operation!")

def bye():
    print("Thanks for using. BYE!")

greet()
user_input()
bye()


        

    