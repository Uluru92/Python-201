# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

def is_integer(user_input):
  try:
    int(user_input)
    return True
  except ValueError:
    return False

user_input = 1
dict_key_n = {}

while user_input != 0:
  user_input = input("type a number:")
  if is_integer(user_input) == True:
    user_input_int = int(user_input)
    dict_key_n[user_input_int] = user_input_int*user_input_int
    sorted_dict_key_n = sorted(dict_key_n.items())
    print("Dictionary update:",sorted_dict_key_n)
  else:
    print("Please introduce an integer number:")
  user_input = 1

  