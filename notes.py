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
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide a valid input"  
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return(f"Result: {formatted_f_name} {formatted_l_name}")
    print("This got printed")

print(format_name(input("what is your first name? "), input("what is your last name? ")))