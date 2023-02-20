"""
This is the calculator 
"""


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    if n2 == 0:
        return "Your input cann't be zero"
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print("Here is the LOGO")
    num1 = float(input("What is your first number : "))
    for operator in operations:
        print(operator)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What is your next number : "))
        calculation_function = operations[operation_symbol]
        anwser = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {anwser}")

        if input(f"Type 'y' for calculating with {anwser} or type 'n' to a new calculation : ") == "y":
            num1 = anwser
        else:
            should_continue = False
            calculator()  # Call function itself :  Recursion in programing


calculator()
