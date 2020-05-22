cel_temp = int(input("Please enter the integer temperature value: "))


def fahrenheit(var_cel_temp):
    return (18 * var_cel_temp + 320) / 10


print("The Fahrenheit equivalent of " + str(cel_temp) + " degrees Celsius is " + str(fahrenheit(cel_temp)))


