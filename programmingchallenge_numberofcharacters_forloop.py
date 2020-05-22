user_string = input("Please enter a String.")
number_of_characters = 0

for letter in user_string:
    number_of_characters = number_of_characters + 1

print(user_string)
print("The number of characters in the input string is: " + str(number_of_characters))
