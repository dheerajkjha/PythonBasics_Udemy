# 1. Generic Module Import - Imports the module

import random
print(random.randint(12, 22)) # Generate random integers between 12 and 22 both inclusive

# 2. Function Import - Imports the Function in a Module
from random import randint
print(randint(10, 20))

# 3. Universal Import - Imports all functions of a module
from random import *
print(random())
print(randrange(25, 50, 4))

