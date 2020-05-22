list_one = [1, 2, 3, 4]
list_two = [1.2, 3.14, 4.66]
list_three = [True, False]
list_four = ["Victoria", "Melbourne"]
list_five = [[1, 2], [3, 4, 5]]
list_six = [1, "Dheeraj", True, 5568.99, [15, "July", 1989]]
print(list_one)
print(list_two)
print(list_three)
print(list_four)
print(list_five)
print(list_six)

# in function
print(3.14 in list_two)  # True
print(False not in list_six)  # True

# indexes in list
print(list_six[4])  # [15, 'July', 1989]
print(list_six[4][1])  # July
print(list_six[4][1][0])  # J

# Negative indexes
print(list_six[-1])   # [15, 'July', 1989]
print(list_six[-1][-2])  # July
print(list_six[-1][-2][-3])  # u

# Items accessed by Index in expressions
print(list_two[1] + 3.14)  # 6.28
print("I am currently staying in \"" + list_four[1] + "\".")  # I am currently staying in "Melbourne".

# List slicing
print(list_six[:3])  # [1, "Dheeraj", True]
print(list_six[1:4])  # ['Dheeraj', True, 5568.99]
print(list_six[2:])  # [True, 5568.99, [15, 'July', 1989]]

# Assigning new values to the list
list_old = [1, 3, 5, 7, 9, 11]
print(list_old)  # 1, 3, 5, 7, 9, 11]
list_old[2] = 4
print(list_old)  # [1, 3, 4, 7, 9, 11]

# New element got added to the list when the old list is sliced and assigned new values
list_old[3:7] = [8, 8, 8, 8]
print(list_old)  # [1, 3, 4, 8, 8, 8, 8]

# del method - Deletes the element from the list and shift the entire list to the left
# from the place where item is deleted
del list_old[0]
print(list_old)  # [3, 4, 8, 8, 8, 8]


# .remove method - Deletes the element from the list and shift the entire list to the left
# # from the place where item is deleted
list_old.remove(3)
print(list_old)  # [4, 8, 8, 8, 8]

# If we pass a argument in remove method which is present more than once in the list
# the first occurrence will be deleted
list_old.remove(8)
print(list_old)  # [4, 8, 8, 8]

# .append() method - Adds an item at the end of the list
list_old.append("Melbourne")
print(list_old)  # [4, 8, 8, 8, 'Melbourne']

# .insert() method - Adds an item anywhere in the list
list_old.insert(5, 9.99)
print(list_old)
list_old.insert(2, "Phantom")
print(list_old)

# .sort() - To sort the list made of either the integers or strings
list_new_num = [12, 32, 555,1, 0, -1 -55]
list_new_str = ["My", "name", "is", "Melbourne"]
print(list_new_num.sort())  # None
print(list_new_str.sort())  # None
list_new_str.sort()

list_new_num.sort()
print(list_new_num)  # [-56, 0, 1, 12, 32, 555]
print(list_new_str)  # ["My", "name", "is", "Melbourne"]
list_new_str.sort(key=str.lower)
print(list_new_str)  # ['is', 'Melbourne', 'My', 'name']

# ASCIIbetical order - sorting
# Reversing in the String also changes based on the word
# staring with capital or small letters
# All words starting with Capital letters are sorted and then with small letters

# reverse = true - This will sort the items in the reverse order
list_new_str.sort(reverse=True)
list_new_num.sort(reverse=True)
print(list_new_num)  # [555, 32, 12, 1, 0, -56]
print(list_new_str)  # ['name', 'is', 'My', 'Melbourne']

# mixed sort -  List with mixed data types are not supported in Python
# But True (Boolean = 1) and False (Boolean = 0)
mixed_list = [-9, False, True, -7, 55, 0.77]
mixed_list.sort()
print(mixed_list)  # [-9, -7, False, 0.77, True, 55]

# .index() - Return the index number of the String from the list passed as an argument
print(mixed_list.index(55))  # 5

# .pop() method removes/deletes the item from the list and
# return the removed/deleted item
popped_item = mixed_list.pop(1)
print(mixed_list)  # [-9, False, 0.77, True, 55]
print(popped_item)  # -7
popped_item_new = mixed_list.pop()
print(mixed_list)  # [-9, False, 0.77, True]
print(popped_item_new)  # 55
# If non index number is mentioned in the pop(), it
# removes and returns the last value from the list

