def factorial_func(num):
    fact = 1
    for fact_counter in range(num, 1, -1):
        fact = fact * fact_counter
    print(fact)
    return fact


factorial_func(5)
factorial_func(4)
factorial_func(3)