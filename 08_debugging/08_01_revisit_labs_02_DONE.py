#Pick at least three labs and do them again while actively using a debugger.

#Revisit the labs that you had a hard time completing.
#Start them over from scratch without looking at the solution.

#Use a visual debugger, such as the one integrated in your IDE or any
#of the other options mentioned in the course to while writing the
#code for these tasks.

#This will give you a chance to revisit challenging tasks, as well as
#to train using your debugger tool.

#Pick 2: Re-Solution to exercise 06_11_floored_generetor

nums = (x for x in range(1, 1000000))
for x in nums:
    print("x=",x, "-> x/1111=", x//1111)
