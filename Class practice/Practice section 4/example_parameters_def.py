# how to call a def with different inputs

def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

print(greet("Hello", "Jorddy"))  # Hello, World! How are you?
print(greet("Howdy", "partner"))  # Howdy, partner! How are you?
print(greet("Zdravo", "prijatelj"))  # Zdravo, prijatelj! How are you?
print(greet("Hi", "Martin"))  # Hi, Martin! How are you?