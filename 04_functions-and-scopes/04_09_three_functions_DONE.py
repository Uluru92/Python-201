# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def welcome(message_1, *args):
    greetings = ""
    for name in args:
        sentence = f"\n{message_1} {name}! come inside please!"
        greetings += sentence + "\n"
    print(greetings)
    return greetings

def welcome_and_give_menu(*args):
    welcome("Welcome!", "Jorddy", "Fabián")
    food_menu = "This is the Food Menu:"
    print(food_menu)
    for item in args:
        print(item)
    return food_menu

def total_service_premium(cost):
    welcome_and_give_menu("king hamburger","premium hot dogs","extra large pizza")
    message_3 = f"\nThe total cost is {cost}$\n"
    print(message_3)
    return message_3

print("\nFUNCTION 1: \n")
welcome("Hey!","Fernando","María")

print("\nFUNCTION 2: \n")
welcome_and_give_menu("Pasta","Beef","Pork")

print("\nFUNCTION 3: \n")
total_service_premium("150")