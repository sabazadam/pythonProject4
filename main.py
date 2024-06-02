def add(a,b):
    return a + b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def substract(a,b):
    return a - b

number1 = int(input("Give me a number: "))
number2 = int(input("Give me the second number: "))
my_dictionary = {
    "+": add(number1,number2),
    "*":multiply(number1,number2),
    "-":substract(number1,number2),
    "/": divide(number1,number2)
                 }
