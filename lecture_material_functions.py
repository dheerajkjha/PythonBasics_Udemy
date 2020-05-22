# Defining a function
def func_sum():
    print(12 + 2)


# As per Python style guide, two line separation after function definition
# Calling a function
func_sum()

input_var_string = "The number "


def concat_func(p1, p2, p3):
    print(p1 + str(p2) + p3)


concat_func(input_var_string, 10, " is an Integer.")


def default_value_func(num1=6, num2=8):
    print(num1 * num2)


default_value_func()
default_value_func(5)
default_value_func(3, 6)


def return_func(num1=4, num2=5):
    return num1 * num2


print(return_func() + 10)

