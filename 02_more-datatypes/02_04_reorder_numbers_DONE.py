# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

print("Please introduce 10 numbers!:")
number_1 = int(input(("Number 1:")))
number_2 = int(input(("Number 2:")))
number_3 = int(input(("Number 3:")))
number_4 = int(input(("Number 4:")))
number_5 = int(input(("Number 5:")))
number_6 = int(input(("Number 6:")))
number_7 = int(input(("Number 7:")))
number_8 = int(input(("Number 8:")))
number_9 = int(input(("Number 9:")))
number_10 = int(input(("Number 10:")))

list_ = [number_1,number_2,number_3,number_4,number_5,number_6,number_7,number_8,number_9,number_10]
list_reordered = [list_[1],list_[3],list_[5],list_[7],list_[9],list_[8],list_[6],list_[4],list_[2],list_[0]]

print("Input:", list_)
print("output:",list_reordered)
