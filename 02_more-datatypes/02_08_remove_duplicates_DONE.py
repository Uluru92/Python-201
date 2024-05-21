# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:

list_ = [1, 2, 3, 4, 3, 4, 5]

# 1. Convert to a different data type
list_set = set(list_)
new_list = list(list_set)
print("the new list witout duplicates:", new_list)

# 2. Use a loop and a second list to solve it more manually
new_list_2 = list()
for element in list_:
    if element not in new_list_2:
        new_list_2.append(element)
print("the new list witout duplicates:", new_list_2)
