# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

#pseudocodigo:
#abrir el archivo... en modo r... guardar todas las lineas en una lista...
#abrir un nuevo documento... en modo w... y empujarle todas palabras de la lista aldervez

from pathlib import Path
file_words_path = Path("Python-201-main/03_file-input-output/words.txt")

words=[]
with open(file_words_path, "r") as file_words:
    for word in file_words.readlines():
        new_word = word.strip()
        words.append(word)

reversed_words=words[::-1]

with open("Python-201-main/03_file-input-output/words_reverse.txt", "a") as file_reverse_words:
    for word in reversed_words:
        file_reverse_words.write(word)
