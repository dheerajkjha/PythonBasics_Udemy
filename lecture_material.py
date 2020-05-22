print("Hello Dheeraj Kumar Jha")  # Dheeraj Kumar Jha

# Printing 4^4 or 4 * 4 * 4 * 4
print(4 ** 4)  # 256

# Printing quotient of 17/3
print(17 // 3)  # 5

# Printing remainder of 18/4
print(18 % 4)  # 2

# Printing quotient of 4/-2
print(4 // -2)  # -2

# Understanding the Operator precedence
print((9-7) * 2 ** 3 + 10 % 6 // -1 * 2 - 1)  # 7

# Understanding approximation error when working with floats
print(1.23 + 2.80)  # 4.029999999999999

# Using multiplication by 100 to overcome approximation error
print((123+280)/100)  # 4.03

# Using round() function to overcome approximation error
exampleRound = 1.23 + 2.80
print(round(exampleRound, 2))  # 4.03
print(round(exampleRound, 3))  # 4.03

# Indexing in String, to access particular letter in the String
example_string = "Orange"
print(example_string[1])  # r
print("apple"[4])  # e

# String slicing or sub string
example_string_2 = "Programming Language"
# Substring from first letter to 7th letter
print(example_string_2[:7])   # Program
# Substring from 5th letter to 11th letter
print(example_string_2[4:11])  # ramming
# Substring from 8th letter to the end of the String
print(example_string_2[8:])  # ing Language

# String Concatenation
print("Dheeraj" + " " + "Kumar" + " " + "Jha")  # Dheeraj Kumar Jha

# type() function
var_one = True
var_two = 1
var_three = 2.3445
var_four = "Let's Play"
print(type(var_one))  # <class 'bool'>
print(type(var_two))  # <class 'int'>
print(type(var_three))  # <class 'float'>
print(type(var_four))  # <class 'str'>

# str() function
var_five = True
print(type(str(var_five)))  # <class 'str'>
print(type(var_five))  # # <class 'bool'>

# Escape Sequences
# \t - tab space
print("Dheeraj\tKumar\tJha")  # Dheeraj	Kumar	Jha

# \n - new line
print("Good Night\nSleep better!")
# Good Night
# Sleep better!

# \' and \" - Single and double quotes
print("\"Lucy\'s Magnet\"")  # "Lucy's Magnet"
print('\'Working hard does not matter\', \"Smart does\"')  # 'Working hard does not matter', "Smart does"

# \\ - To put only the backslash
print("https:\\\google.com")  # https:\\google.com

# input() - To get the inout from the user
name = input("Please enter your name - ")
print("The entered name is - " + name)  # Jaya Mishra
print(type(name))  # <class 'str'>

# int() function
user_int_var = input("Please enter an integer.")  # 7
print(user_int_var)  # 7
print(type(user_int_var))  # <class 'str'>

user_int_var = int(input("Please enter an integer."))  # 2
print(int(user_int_var))  # 2
print(type(user_int_var))  # <class 'int'>

# user_str_var = int(input("Please enter your name."))  # Error
# print(user_str_var)
# print(type(user_str_var))

print(int(11.5))  # 11

# float() function
user_flo_val = input("Please enter a decimal value")  # 11.7
print(user_flo_val)  # 11.7
print(type(user_flo_val))  # <class 'str'>

user_flo_val = float(input("Please enter a decimal value"))  # 15.7
print(user_flo_val)  # 15.7
print(type(user_flo_val))  # <class 'float'>

print(float(11))  # 11.0













