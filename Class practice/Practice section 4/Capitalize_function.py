sentence = "lets capitalize every word in this sentence"

def cap_words (text):
    healine_word = []
    for word in text.split():
        cap_word = word.capitalize()
        healine_word.append(cap_word)
    return " ".join(healine_word)

capitalized_test = cap_words(sentence)
print(capitalized_test)

