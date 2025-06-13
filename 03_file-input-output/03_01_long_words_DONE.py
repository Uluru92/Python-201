# Write a program that reads in `words.txt` and prints only the words.
# that have more than 20 characters (not counting whitespace).

from pathlib import Path

file_words_path = Path("03_file-input-output/words.txt")

words = []
with open(file_words_path, "r") as file_words:
    for word in file_words.readlines():
        word = word.strip()
        if word.__len__()>20:
            words.append(word)
for w in words:
    print(w, "with", len(w),"chars!")

