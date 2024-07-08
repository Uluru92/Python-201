# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages




def by_4_or_7(number_user):
    number_user = 0
    while number_user not in [1,1000000000]:
        number_user = int(input("Enter a number between 1 and 1,000,000,000: "))
        if 1 <= number_user <= 1000000000:
            print(f"Lets see if your number {number_user} is divisible by 4 or 7...")
            residuo_4 = number_user%4
            residuo_7 = number_user%7
            if residuo_4 == 0 and residuo_7 != 0:
                print(f"Your number {number_user} is divisible by 4!")
            elif residuo_4 != 0 and residuo_7 == 0:
                print(f"Your number {number_user} is divisible by 7!")
            elif residuo_4 == 0 and residuo_7 == 0:
                print(f"Your number {number_user} is divisible by 4 and 7!")
            elif residuo_4 == 0 and residuo_7 == 0:
                print(f"Your number {number_user} is divisible by 4 and 7!")
            else:
                print(f"Your number {number_user} is not divisible by 4 and 7!")
        else:
            print("Please enter a number between 1 and 1,000,000,000")

by_4_or_7(0)
