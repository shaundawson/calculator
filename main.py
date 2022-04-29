from art import logo
from replit import clear

print(logo)

#This function adds two numbers
def add(n1, n2):
    return n1 + n2

#This function subtracts two numbers
def subtract(n1, n2):
    return n1 - n2

# This function multiplies two numbers
def multiply(n1, n2):
    return n1 * n2

#This function divides two numbers
def divide(n1, n2):
    return n1 / n2

#Store operator functions in a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1= int(input("What\'s the first number? "))
#Loop through dictionary and print out each key.
for symbol in operations: 
    print(symbol)
operations_symbol = input("Pick an operation: ")
num2 = int(input("What\'s the next number? "))

#Determine which calculation to use
calculation_function = operations[operations_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operations_symbol} {num2} = {answer}")