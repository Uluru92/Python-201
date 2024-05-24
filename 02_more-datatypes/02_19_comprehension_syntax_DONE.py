# Use a list comprehension to create a list that contains the individual
# letters of the word "codingnomads":
# ['c', 'o', 'd', 'i', 'n', 'g', 'n', 'o', 'm', 'a', 'd', 's']

word = "codingnomads"
print("word:",word)

# Note: You can solve this more quickly with a call to `list()`
word_list = list(word)
print("letters list 1:",word_list)

# but try to do it using a list comprehension.
word_list_2 = list()
for i in word:
    word_list_2.append(i)

print("letters list 2:",word_list_2)