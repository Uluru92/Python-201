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

def greet_many_using_tuples(greeting, *args):
    greetings = ""
    for names in args:
        sentence = f"{greeting}, {names}! good morning!"
        greetings += sentence + "\n"
    return greetings

tuple_names = ("Jorddy", "Carlos", "Brayam")
Hello_tuples = greet_many_using_tuples("Hey!!!", tuple_names[0],tuple_names[1],tuple_names[2])
print(Hello_tuples)