# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = list()
list_items = sorted(input_dict)
print("input_dict:",input_dict)
print("list_items",list_items)
list_items_sorted_by_values = sorted(list_items, key=input_dict.__getitem__)
print("list_items_sorted_by_values:",list_items_sorted_by_values," and its type is:", type(list_items_sorted_by_values))
counter = 0
while counter <= list_items_sorted_by_values.__len__()-1:
    new_word = str(list_items_sorted_by_values[counter])
    print("new_word",new_word,"type:",type(new_word))
    new_list = list()
    new_list.append(new_word)
    new_list.append(input_dict[list_items_sorted_by_values[counter]])
    print("new_list",new_list)
    new_tuple = tuple(new_list)
    result_list.append(new_tuple)
    new_list=list()
    new_tuple=tuple()
    counter+=1
print("result_list:",result_list)