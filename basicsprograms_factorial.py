num = int(input("Enter a number."))


def num_factorial(number):
    inti_fact = 1
    if number == 0:
        print("Factorial of {0} is : {1}".format(number, inti_fact))
        return inti_fact
    else:
        for count in range(num, 0, -1):
            inti_fact = inti_fact * count
        print("Factorial of {0} is : {1}".format(number, inti_fact))
        return inti_fact


num_factorial(num)
