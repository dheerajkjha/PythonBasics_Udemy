# To convert string to all lower case
var_str_one = "My name is Dheeraj Kumar Jha"
print(var_str_one.lower())

# To convert string to all upper case
print(var_str_one.upper())

# To convert the String in title case
print("going to australia".title())  # Going To Australia

# To check if the string has all upper/lower case letters
# .isupper() or .islower() methods will only return true/false
# if the string has at least one letter.
# If the sting is blank or only has number/special characters
# it will return false
var_str_two = "100 AUSTRALIA"
var_str_three = "100 dj"
print(var_str_two.isupper())  # True
print(var_str_two.islower())  # False
print(var_str_three.islower())  # True
print("".islower())  # False
print("221@@".isupper())  # False

# .isalpha() - To check if the string contains all alphabets
print("Batman".isalpha())  # True
print("Batman12".isalpha())  # False
print("".isalpha())  # False
print("@!!!!".isalpha())  # False

# .isalnum() - To check if the string contains all alphabets and numbers
print("Batman".isalnum())  # True
print("Batman12".isalnum())  # True
print("".isalnum())  # False
print("@!!!!".isalnum())  # False

# .isdecimal() - To check if the string contains all numbers
print("Batman".isdecimal())  # False
print("Batman12".isdecimal())  # False
print("".isdecimal())  # False
print("@!!!!".isdecimal())  # False
print("123".isdecimal())  # True
print("3.14".isdecimal())  # False

# .isspace() - To check if the string contains only spaces
print("   ".isspace())  # True
print("".isspace())  # False
print("Melbourne1@@@".isspace())  # False
print("Not Shown"[3].isspace())  # True

# .istitle() - To check if the string is in title case
print("Melbourne Victoria Australia".istitle())  # True
print("melbourne victoria Australia".istitle())  # False
print("docklands".istitle())  # False

# .startswith()
print("This is Melbourne".startswith("This"))  # True
print("This is Melbourne".startswith("T"))  # True
print("This is Melbourne".startswith("this"))  # False

# .endswith()
print("This is Melbourne.".endswith("Melbourne."))  # True
print("This is Melbourne.".endswith("."))  # True

# .join() - To join different String and returns one complete String
print(" ".join(["The country", "name", "is", "Australia."]))  # The country name is Australia.

# .split() - Split a string based on space by default and returns a list
print("Eggs, Milk, Waffles".split())  # ['Eggs,', 'Milk,', 'Waffles']
print("Eggs, Milk, Waffles".split(","))  # ['Eggs', 'Milk', 'Waffles']

# .ljust() and .rjust()
# Four spaces added to the left. String adjusted to the right.
print("Hello World".rjust(15))  #     Hello World

# Four spaces added to the right. String adjusted to the left.
print("Hello World".ljust(15) + "! Again")  # Hello World    ! Again

# The second argument must be a single character
print("Hello World".rjust(15, "-"))  # ----Hello World
print("Hello World".ljust(15, "#") + "! Again")  # Hello World####! Again

# .centre() - Adds the character/spaces to the right and left of the string
print("Hello World".center(15, "-"))  # --Hello World--

# .strip() - Removes white spaces from both sides of the String
# .lstrip() - Removes spaces from the left side of the String
# .rstrip() - Removes spaces from the right side of the String
print("  Hello Melbourne !  ")  #   Hello Melbourne !
print("  Hello Melbourne !  ".strip())  # Hello Melbourne !
print("  Hello Melbourne !  ".lstrip())  # Hello Melbourne !
print("  Hello Melbourne !  ".rstrip())  #   Hello Melbourne !

print("I play!!")  # I play!!
print("I play!!".strip("!"))  # I play
print("I play!!".rstrip("!"))  # I play
print("I play!!".lstrip())  # I play!!

print("Melbourne, Victoria, Australia")  # Melbourne, Victoria, Australia\
print("Melbourne, Victoria, Australia".rstrip(", Victoria"))  # Melbourne, Victoria, Austral
print("Melbourne, Victoria, Australia".rstrip(", Australia"))  # Melbourne, Victor

# The order in which characters are mentioned in the argument does not matter.
# Strip method keeps checking the string until it does not finds a character to remove from left and right
print("elbublueyelloweubl".strip("leub"))  # yellow

# .replace() - Find a string and replaces with another
print("Good Morning".replace("Morning", "Afternoon"))  # Good Afternoon

# .len() - Gets the length of the string
print(len("Australia Day"))  # 13
print("Australia Day"[3: 10])  # tralia
print(len("Australia Day"[3: 10]))  # 7
