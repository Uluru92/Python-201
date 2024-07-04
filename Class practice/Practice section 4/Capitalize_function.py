sentence = "lets capitalize every word in this sentence"
sentence2 = "i love python"
sentence3 = "quiero tomar cafe con pan"

def cap_words (text):
    healine_word = []
    for word in text.split():
        cap_word = word.capitalize()
        healine_word.append(cap_word)
    return " ".join(healine_word)

capitalized_sentence = cap_words(sentence)
print("sentence:", sentence)
print("capitalized_sentence:", capitalized_sentence)

print(sentence2.title())
print(sentence3.capitalize())

