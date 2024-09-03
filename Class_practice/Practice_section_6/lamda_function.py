#define a regular function
def square_root(x):
    return x**2
print(square_root(5))

#same but in lambda function
squared = lambda x: x**2
print(squared(5))

#compare
print(square_root(4) == squared(4))  # OUTPUT: True

#using lambda with a list of tuples
ingredients = [("carrots", 2), ("potatoes", 4), ("peppers", 1)]
print(ingredients)
print(sorted(ingredients, key=lambda x: x[1]))

#using lambda with ranges
squares = list(map(lambda x: x**2, range(10)))
print(squares)  

#same solution but with a for loop
squares = [x**2 for x in range(10)]
print(squares)  

