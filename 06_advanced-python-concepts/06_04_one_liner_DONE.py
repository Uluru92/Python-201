# Use a one-liner list comprehension to express the following functionality:
#
# letters = []
# for letter in 'suchalongword':
#     letters.append(letter)
# print(letters)

#solution
letters = []
listcomp = [letters.append(letter) for letter in "suchalongword"]
print(letters)