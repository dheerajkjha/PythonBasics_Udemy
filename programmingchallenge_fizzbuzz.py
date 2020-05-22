input_range = range(1, 50)
for num in input_range:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fiz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
