 #100DaysofCode - Day 10 Beginner Functions with Outputs

#Functions with Outputs
# def my_function():
#     result = 3 *2
#     return result
#     output = result

# output = my_function()
# print(output)


# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return(f" {formatted_f_name} {formatted_l_name}")

# formatted_string = format_name("shAUN", "DAWSON")
# print(formatted_string)


#MULTIPLE RETURN VALUES
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide a valid input"  
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return(f"Result: {formatted_f_name} {formatted_l_name}")
#     print("This got printed")

# print(format_name(input("what is your first name? "), input("what is your last name? ")))



#EXERCISE - DAYS IN MONTH
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#     if month > 12 or month < 1:
#         return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month -1]

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


#DOCSTRINGS
#Already used functions with outputs
# length = len(formatted_name)

#Return as an early exit
# def format_name(f_name, l_name):
#     """" Take a first and last name and format it to return the title case version of the name. """
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"Result: {formatted_f_name} {formatted_l_name}"



#EXERCISE - CALCULATOR (Without Dictionary)
from art import logo
from replit import clear

print(logo)

x = int(input("What\'s the first number? "))
operators= ["+", "-", "*", "/"]
print(*operators, sep = "\n")
operator = input("Pick an operation: ")
y = int(input("What\'s the next number? "))

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

is_continue = True  
def calc(x, y):
        while is_continue == True:
        # check if choice is one of the four options        
            if operator == '+':
                print(x, "+", y, "=", add(x, y))
                return
        
            elif operator == '-':
                print(x, "-", y, "=", subtract(x, y))
                return
        
            elif operator == '*':
                print(x, "*", y, "=", multiply(x, y))
                return
        
            elif operator == '/':
                print(x, "/", y, "=", divide(x, y))
                return

calc(x,y)

stop_game = input("Type 'y' to continue calculating or type 'n' to start a new calculation: \n")
if stop_game == "n":
    is_continue = False
    clear()
