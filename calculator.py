"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""
from arithmetic import *


calculating = True

while calculating:
    user_input = input("Input operator and numbers for calculation here: ")

    if len(user_input) == 1 and user_input == "q":
        break

    calculator_tokens = user_input.split(" ")

    operator = str(calculator_tokens[0])
    num1 = float(calculator_tokens[1])

    
    if len(calculator_tokens) > 3:
        print("Too many inputs, invalid")
        calculating = False
    elif len(calculator_tokens) < 2:
        print("Too few inputs, invalid")
        calculating = False
    else:
        if len(calculator_tokens) == 3:
            num2 = float(calculator_tokens[-1])

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "mod":
            result = mod(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "square":
            result = square(num1)
        elif operator == "cube":
            result = cube(num1)
        elif operator == "pow":
            result = power(num1, num2)

        print(result)
