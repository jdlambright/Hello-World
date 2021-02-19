#from replit import clear... this only worked in the replit environment
from art import logo

#functions for each operator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

#dictionary of functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#primary function
def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    #while loop that allows user to continue calculating based of results
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        #this tells the program to end or continue
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            #clear()
            calculator()

#this makes it a function that calls itself aka recursive fi
calculator()
