# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
string_tuple = tuple(string)
string_list = list(string_tuple)

print("string:",string,"type:",type(string))
print("tupple:",string_tuple,"type:",type(string_tuple))
print("list:",string_list,"type:",type(string_list))

string_list[0] = "k"
print("list:",string_list,"type:",type(string_list))

string_tuple = tuple(string_list)
print("tupple:",string_tuple,"type:",type(string_tuple))
