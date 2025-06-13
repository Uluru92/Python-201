# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

#pseudocodigo:
#abrir el archivo... en modo r... guardar todas las lineas en una lista...
#abrir un nuevo documento... en modo w... y empujarle todas palabras de la lista aldervez

from pathlib import Path
file_words_path = Path("03_file-input-output/words.txt")

words=[]
with open(file_words_path, "r") as file_words:
    for word in file_words.readlines():
        words.append(word)

words[words.__len__()-1] = words[words.__len__()-1]+"\n"
words[0] = words[0][:2]
reversed_words=words[::-1]

with open("03_file-input-output/words_reverse.txt", "a") as file_reverse_words:
    for word in reversed_words:
        file_reverse_words.write(word)