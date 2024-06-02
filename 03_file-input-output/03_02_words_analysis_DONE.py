# Read in all the words from the `words.txt` file.
# Then find and print:

from pathlib import Path
file_words_path = Path("Python-201-main/03_file-input-output/words.txt")

# 1. The shortest word (if there is a tie, print all)
shortest_len = int(1000)
new_shortest_len = int()
with open(file_words_path, "r") as file_words:
    for word in file_words.readlines():
        new_word = word.strip()
        if shortest_len > new_word.__len__():
            new_shortest_len = new_word.__len__()
            shortest_len = new_shortest_len
    print("all the shortest words with",shortest_len,"chars:")

short_words = []
with open(file_words_path, "r") as file_words:
    for word in file_words.readlines():
        word = word.strip()
        if word.__len__() ==shortest_len:
            short_words.append(word)
for w in short_words:
    print(w)

# 2. The longest word (if there is a tie, print all)
longest_len = int(0)
new_longest_len = int()
with open(file_words_path, "r") as file_words:
    for word in file_words.readlines():
        new_word = word.strip()
        if longest_len < new_word.__len__():
            new_longest_len = new_word.__len__()
            longest_len = new_longest_len
    print("all the longest words with",new_longest_len,"chars:")

long_words = []
with open(file_words_path, "r") as file_words:
    for word in file_words.readlines():
        word = word.strip()
        if word.__len__() ==longest_len:
            long_words.append(word)
for w in long_words:
    print(w)

# 3. The total number of words in the file
counter = 0
with open(file_words_path, "r") as file_words:
    for word in file_words.readlines():
        counter +=1
print("The total number of words in the file:", counter)