# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

def is_integer(user_input):
  try:
    int(user_input)
    return True
  except ValueError:
    return False
  
set_=set()
user_input = 1
life_points = int(5)

print("Welcome to the MEMORY GAME:")
print("Rules:")
print("  -You need to introduce 10 numbers from 1 to 15 without duplicates")
print("  -If you repeat a number you lose 1 point life")
print("  -You start with:",life_points)

while is_integer(user_input) == True and set_.__len__()<11:
    user_input = input("type a number:")
    if is_integer(user_input) == True:
       user_input_int = int(user_input)
       if user_input_int not in set_ and user_input_int > 0 and user_input_int < 16:
          set_.add(user_input_int)
          user_input_int = None
          if set_.__len__()==10:
             print("You won!")
       elif user_input_int < 1 or user_input_int > 15:
           print("Please enter a number between 1 and 15")
       else:
         life_points-=1
         print("Your input is a duplicate, you got a deducted life point for a total of:", life_points)
         if life_points == 0:
            print("You lost!")
    else:
       print("Please introduce an integer number between 1 and 15")
    user_input = 1