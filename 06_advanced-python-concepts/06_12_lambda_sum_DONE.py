# Write a lambda expression that takes in three numbers
# and returns the sum of the numbers.

#solution
sum = lambda x,y,z:x+y+z
print("Lets sum three numbers by using a lambda expresion!")
print("result:",sum((int(input("introduce the first number:"))),(int(input("introduce the second number:"))),(int(input("introduce the third number:")))))