def print_args(*argumentos): #you can use any variable name...  
    for a in argumentos:     #but...for everyone's sake, just stick with args
        print(a)             #to help others and yourself remember 
                             #the language feature you're using.

print_args("apta 1", "apta 2", "apta 3", "apta 4", "apta 5", "airbnb") #modified the *args

# OUTPUT:
# barcelona
# tahoe
# ubud
# koh tao

def greet_many(greeting, *args):
    greetings = ""
    for name in args:
        sentence = f"{greeting}, {name}! good morning!"
        greetings += sentence + "\n"
    return greetings

Hello = greet_many("Hey!!!", "Maria", "Ana", "Jose", "Luis", "Fernando")
print(Hello)
