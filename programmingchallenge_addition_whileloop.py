number = int(input("Please enter an Integer number."))
number_sum = 0
print("Entered number by the user is: " + str(number))
while number > 0:
    number_sum = number_sum + number
    number = number - 1
print("Sum of the numbers from the entered number and 1 is: " + str(number_sum))
