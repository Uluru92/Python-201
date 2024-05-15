# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"
string_to_tupple = tuple(string)

print("iterate over your string, this is what happens:")
for i in string:
    print(i)

print("iterate over your tuple, this is what happens:")
for i in string_to_tupple:
    print(i)

print("WELL, SEEMS LIKE THERE IS NO DIFFERENCE MY FRIEND...")


