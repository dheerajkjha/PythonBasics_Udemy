name = input("Please enter the name.")
degree = input("Please mention the major degree.")
job = input("Please enter the job position.")
years = input("Please enter the number of years in th job.")

print(name + " majored in " + degree + ", works as a " + job + ", and has " + years + " years of experience.")

# Using .format() method
print("{} majored in {}, works as a {}, and has {} years of experience.".format(name, degree, job, years))
