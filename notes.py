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
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month -1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)