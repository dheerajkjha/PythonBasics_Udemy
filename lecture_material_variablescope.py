# 1. Local variables cannot be used by code in the global scope.
def func_name1():
    breakfast = "Waffles"
    return breakfast

# func_name1()
# print(breakfast)  # Error - name 'breakfast' is not defined

# 2. Global variables can be accessed by code in a local scope.


def print_glob():
    print(var_name)


var_name = "Good Morning!"
print_glob()


# 3. The local scope of one function can't use variables from another function's
# local scope.
def loc_sc1():
    loca_var = "fruit"
    print(loca_var)


# def loc_sc2():
#    print(loca_var)


loc_sc1()
# loc_sc2()


# 4. Same name can be used for different variables as long as they are
# in different scope

def fun1():
    var1 = "Apple"
    print(var1)


def fun2():
    var1 = "Banana"
    print(var1)


var = "Orange"
fun1()
fun2()
print(var)


# 5. To change the scope of local variable to global
def new_fun():
    global var_name  # This statement will make the var_name variable in local scope as global
    var_name = "Testing"
    print(var_name)


var_name = "Important"
new_fun()
print(var_name)





