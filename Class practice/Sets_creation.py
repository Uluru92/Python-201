set_1 = {1,2,33,44,55,66,77,88,88,88} #because it is a set, all repetitive elements are gone automatically
print("set_1:",set_1)

set_2 = set() # to create an empty set this is how! otherway... if you use {} you are actually creating an empty dictionary!
print("set_2:",set_2)
print("set_2 TYPE:",type(set_2))

set_3 = {} # This is how you create an EMPTY DICTIONARY
print("set_3 TYPE:",type(set_3))

list_A = [1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 8,8,8,9] # list with repetitive elements
print ("List_A", list_A, "is a", type(list_A))

set_A = set(list_A) #This way we can eliminate the iteratives elements of a list and make them uniques
print("set_A", set_A, "is a", type(set_A))
list_B = list(set_A)
print("List_B", list_B, "is a", type(list_B))

set_A_1 = set_A|set_1 #Returns a new set that contains all elements of set_A and set_1.
print("set_A_1:", set_A_1)

set_x = ["x","xx","xxx"]
set_A_1_X = set_A_1.union(set_x)
print("set_A_1_X:",set_A_1_X)

set_B = ["b","b","bbb","bbbbb"]
print(set_B)
set_B.append(set_1)
print("set_B_1:",set_B)

set_1_A_intersection = set_1 & set_A #return the elements that have place in both sets!
print("set_1_A_intersection:", set_1_A_intersection)
