# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

random_list = randlist
print("random list:",random_list)

largest_number = max(random_list)
print("The largest number in the list:", largest_number)

product = 1
for i in random_list:
    product *= i

print("The product of all of the numbers in the list:", product)