input_string = input("Please enter a String to be reversed.")
reversed_string = ""
string_range = range(len(input_string)-1, -1, -1)

for counter in string_range:
    reversed_string = reversed_string + input_string[counter]

print(reversed_string)
