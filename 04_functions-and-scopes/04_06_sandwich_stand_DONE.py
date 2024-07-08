# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread, *args):
    ingredients = ""
    for toppings in args:   
        composition = f"{toppings}\n"
        ingredients += composition
    sandwich = "\n" + bread + "\n" + ingredients + bread + "\n"
    print(sandwich)

make_sandwich("Italian Bread", "Tomate","Lettuce","Sauce","Chicken")