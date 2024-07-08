# how to call a def with different inputs

def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

#Order matters by you can uou can also pass arguments
#together with their parameter names as keyword arguments

print(greet("Hello", "Jorddy"))  # Hello, World! How are you?
print(greet(name="Jorddy", greeting="Hello"))

print(greet("Howdy", 777))  # Howdy, partner! How are you?
print(greet(name=888, greeting="Howdy"))

print(greet("Zdravo", "prijatelj"))  # Zdravo, prijatelj! How are you?
print(greet(name="prijatelj", greeting="Zdravo"))

print(greet("Hi", "Martin"))  # Hi, Martin! How are you?
print(greet(name="Martin", greeting="Hi"))