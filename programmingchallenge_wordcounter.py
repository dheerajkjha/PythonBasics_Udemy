# input_string = input("Please enter a String")

input_string = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

list_string = ""

for char in input_string:
    if char.isalpha() or char.isspace():
        list_string = list_string + char


words = list_string.split()
num_words = len(words)

print(words)
print(num_words)


