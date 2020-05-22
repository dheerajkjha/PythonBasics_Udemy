mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())  # False
print(mixed_case.islower())  # False
print(mixed_case.upper())  # A SONG OF ICE AND FIRE
print(mixed_case.lower())  # a song of ice and fire
print(mixed_case.istitle())  # False
title_case = mixed_case.title()
print(title_case)  # A Song Of Ice And Fire
print(mixed_case.startswith("A"))  # True
print(mixed_case.endswith("e"))  # True
words = mixed_case.split()
print(words)  # ['A', 'Song', 'of', 'Ice', 'and', 'Fire']
print(" ".join(words).isalpha())  # False
print("".join(words).isalpha())  # True



