# This is a calculator Project

import os

from art import logo
#print(logo)


# Functions for the arithmetc

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

# Create a dictionary where the keys are the arithmetic symbols and the functions are the values

operators = {
              "+" : add,
              "-" : subtract,
              "*" : multiply,
              "/" : divide,
}

# Introducing an empty function that we shall call later 
def calculator():
    print (logo)
    
    # User Inputs
    num1 = float(input("Enter the first number\n"))

    # Loop through the dictonary and print the the keys coz for loops loop through the dictionary keys
    for symbol in operators:
        print(symbol)
        
    should_continue = True
        
    # while loop

    while should_continue:  
        # Ask user to choose a symbol
        operation_symbol = input("Enter the operator you would like to use\n")

        # Another user input
        num2 = float(input("Enter the next number\n"))

        # Getting the answer
        calculation_function = operators[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        #Incase a user wants to continue with answer
        continue_calc = input("Type 'y' to continue or 'n' to stop\n").lower()
        
        if continue_calc == "y":
            num1 = answer
        else:
            should_continue = False
            os.system('cls')
            calculator()
        
calculator()

