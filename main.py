def add(a,b):
    return a + b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def substract(a,b):
    return a - b

my_dictionary = {
    "+": add,
    "*":multiply,
    "-":substract,
    "/": divide
                 }
number1 = int(input("What is the first number: "))
for sembol in my_dictionary.keys():
    print(sembol)
option = input("Pick operation from the line above? -> ")
number2 = int(input("What's the second number?: "))

result = 0
if option in my_dictionary.keys():
    function = my_dictionary[option]
    result = function(number1,number2)
    print(f"{number1} {option} {number2} = {result}")

while True:
    response = input("type 'q' to exit or type 'y' to continue: ")
    if response == "q":
        print("BYE! ")
        break
    number1 = int(input("What is the number: "))
    for sembol in my_dictionary.keys():
        print(sembol)
    option = input("Pick operation from the line above? -> ")
    function = my_dictionary[option]
    temp_result = result
    result = function(result,number1)
    print(f"{temp_result} {option} {number1} = {result}")
