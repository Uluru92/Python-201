# Write a program that reads in `words.txt` and prints only the words.
# that have more than 20 characters (not counting whitespace).

from pathlib import Path

file_words_path = Path("Python-201-main/03_file-input-output/words.txt")

words = []
with open(file_words_path, "r") as file_words:
    for word in file_words.readlines():
        if word.__len__()>20:
            word = word.strip()
            words.append(word)

for w in words:
    print(w)

