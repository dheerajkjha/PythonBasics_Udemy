the_string = "North Dakota"
print(the_string.rjust(17))  #      North Dakota

print(the_string.ljust(17, "*"))  # North Dakota*****

centre_plus = the_string.center(16, "+")
print(centre_plus)  # ++North Dakota++

print(the_string.lstrip("North "))  # Dakota
print(the_string.rstrip("+"))  # North Dakota

print(the_string.strip("+"))  # North Dakota

print(the_string.replace("North", "South"))  # South Dakota
