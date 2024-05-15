# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
print("List:",list_)

set_unique_list = set(list_) #this way we eliminate the duplicated items inside the list!
print("set_unique_list:",set_unique_list)

unique_list = list(set_unique_list)#then we need to transform back the unique set into a unique list!
print("unique_list:",unique_list)