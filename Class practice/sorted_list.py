#Sorting Basics

list_=[5, 2, 3, 1, 4]
print(list_)
list_ = sorted(list_) #this function accepts any iterable.
print(list_)

a = [5, 2, 3, 1, 4]
print(a)
a.sort() #this method is only defined for lists. 
print(a)

b = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
print(b)
print(type(b))
print(b[3])
b = sorted(b) #sort the dictionary but transform it into a list..... do I lose the values or what???
print(b)
print(type(b))
