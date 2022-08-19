from art import logo

print(logo)


# CALCULATOR
# ADD
def add(x, y):
    return x + y

# SUBTRACT
def subtract(x, y):
    return x - y

# MULTIPLY
def multiply(x, y):
    return x * y

# DIVIDE
def divide(x, y):
    return x / y

def printOps():
    for op in operations:
        print(op)
        
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    continueCalc = True
    num1 = float(input('What is the first number?: '))
    printOps()
    
    while continueCalc:
        operation = input(f"Pick an operation: ")
        num2 = float(input('What is the next number?: '))
        calcFunc = operations[operation]
        answer = calcFunc(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        proceed = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'e' to exit calculator: ")
        if proceed == 'n':
            continueCalc = False
            calculator()
        elif proceed == 'y':
            num1 = answer
        else:
            continueCalc = False

calculator()