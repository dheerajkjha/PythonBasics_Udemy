from random import *
gallonUsed = randint(10, 25)
milesDriven = randint(200, 400)
print("Number of gallons of Gas: " + str(gallonUsed))
print("Miles travelled by car: " + str(milesDriven))
print(milesDriven//gallonUsed)
