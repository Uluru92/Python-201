# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

string_ = str(input("Please introduce a paragraph:"))
string_split = string_.lower().split()

words_dictionary = {} #we create a dictionary so we an keep track of the words(keys) and the counts of each (values)

for word in string_split:
    if word not in words_dictionary:
        words_dictionary[word] = 0
    words_dictionary[word] += 1

print(words_dictionary)

#getting each, key and value, independently 

most_common_word_count = max(words_dictionary.values())
most_comon_word = max(words_dictionary, key=words_dictionary.get)

print("The most common word:", most_comon_word,"with count number:",most_common_word_count)

#ANOTHER WAY.... GETING FIRST THE WORD AND THE ACCESING THE DICTIONARY VALUE WITH THE KEY (WORD)

most_comon_word2 = max(words_dictionary, key=words_dictionary.get)
most_comon_word2_count = words_dictionary[most_comon_word2]

print("The most common word:", most_comon_word2,"with count number:",most_comon_word2_count)

