# while loop
counter = 0
while counter < 5:
    print(counter)
    counter = counter + 1
print("---------------------------")

# for loop
word = "Dheeraj Kumar Jha"
for letter in word:
    print(letter)
print("----------------------------")

# for loop using range()
user_inp_one = range(5)
# range() with only one parameter means, it will start from 0
# and will go till parameter - 1
for number_count in user_inp_one:
    print(number_count)
print("----------------------------")

user_inp_two = range(1, 7)
# range() with two parameters means, it will start from first parameter
# and will go till second parameter - 1
for num_cou in user_inp_two:
    print(num_cou)
print("----------------------------")

user_inp_three = range(11, 27, 2)
# range() with three parameters means, it will start from first parameter
# and will go till second parameter - 1 with increment of third parameter
for num_count in user_inp_three:
    print(num_count)
