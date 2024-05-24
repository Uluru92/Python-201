# Use a list comprehension to create a list called `positive` from the list
# `numbers` that contains only the positive numbers from the provided list.

numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]

positive_list = []
negative_list = []
for i in numbers:
    if i>0:
        positive_list.append(i)
    elif i<0:
        negative_list.append(i)


print("positive_list:",positive_list)
print("positive_list:",negative_list)