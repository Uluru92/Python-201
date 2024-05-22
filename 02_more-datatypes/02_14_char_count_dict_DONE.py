# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

letter_dictionary = {}
script_ = str(input("Please text some words: "))

for letter in script_:
    if letter not in letter_dictionary:
        letter_dictionary[letter] = 0
    letter_dictionary[letter] += 1
    
del letter_dictionary[" "]
print("result:", letter_dictionary)