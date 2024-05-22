# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

def flatten(data):

  for item in data:
    if isinstance(item, (list, tuple)):
      yield from flatten(item)  # Recursively flatten sublists
    else:
      yield item
  
starter_list = [[1, 2, 3, 4], [5, 6,[7,8,[9,10,11]]], [12, 13, 14]]
print("starter_list:",starter_list)

flattened_list = list(flatten(starter_list))
print("flattened_list:",flattened_list)