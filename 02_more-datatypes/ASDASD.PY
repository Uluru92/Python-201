# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

string_user = str(input("please type some words: "))
string_user_list = list(string_user)
print(string_user_list)
result_list = []
new_word = []
word_tuple = tuple()
counter = 0

for i in string_user_list:
    if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        new_word.append(i)
        print("new word:", new_word)
    if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" or counter == string_user_list.__len__()-1:
        word_tuple = tuple(new_word)
        print("word tuple:", word_tuple)
        new_word = []
        result_list.append(word_tuple)
    word_tuple = tuple()
    counter+=1

print("result_list:", result_list)