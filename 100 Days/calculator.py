# calculator

# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("what is your first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue == True:
        op_symbol = input("Pick a operation: ")
        num2 = float(input("what is the next number? "))
        calculation = operations[op_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {op_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
