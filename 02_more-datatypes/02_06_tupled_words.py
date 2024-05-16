# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

string_user = str(input("please type some words: "))
string_user_split = string_user.split()
print(string_user_split)
list_letters = []

for word in string_user_split:
    string_user_split_split = word.split()
    print(string_user_split_split)
    for letter in word:
        string_user_split_split_split = letter.split()
        print(letter)
        list_letters.append(letter)
        print(list_letters)

list_word = []
result_list = []

for i in string_user:
    if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        list_word += i
        print(list_word)
    elif i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" or i == string_user[-1]:
        tuple_word = tuple(list_word)
        #list_tuple_word = list(tuple_word)
        result_list.append(tuple_word)

print("result_list:", result_list)

words = string_user.split()
word_tuples = []

for word in words:
    word_tuple = (word,)
    word_tuples.append(word_tuple)

print(word_tuples)
