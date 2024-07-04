def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    print(sentence)


def greet2(greeting, name):
    sentence = f"{greeting}, {name}! How are you old friend?"
    print(sentence)
    return sentence

def void_func(message):
    print(message)



saludando = greet("Hey","Be")
saludando = greet2("Hi","Pat")
void_func("hola!!")