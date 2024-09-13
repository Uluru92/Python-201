# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.

#solution

generator_multiply_by_itself = (n*n for n in range(10)) #create a generator object.

print(generator_multiply_by_itself)  #Print the object: <generator object <genexpr> at 0x000001F31EAE9700>

for n in generator_multiply_by_itself: #iterate over the generator object and print out each item.
    print(n)