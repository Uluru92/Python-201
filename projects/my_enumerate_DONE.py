# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

# Solution:

iterable = ['red', 'blue', 'yellow'] # Our 'iterable_element' to test my_enumerate

def my_enumerate(iterable_element):  # add your arguments
      index = 0
      for element in iterable_element:
            print(f"{index}. {element}")
            index += 1 #
      pass

# enumarate(iterable) output:

print("\nenumarate(iterable) output: ")
for index,element in enumerate(iterable, start=0):
      print(f"{index}. {element}")

#my_enumarate(iterable) output:
print("\nmy_enumarate(iterable) output: ")
my_enumerate(iterable)
print(" ")