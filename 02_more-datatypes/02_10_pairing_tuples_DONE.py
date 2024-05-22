# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.

# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.

# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.
# Write your code below here:

from resources import randlist

new_list = list()
tuple_ = tuple()

list_ = randlist
list_sorted = sorted(list_)
print("random list:",list_)
print("list sorted:",list_sorted)
lenght = list_sorted.__len__()
print("La longitud de la lista es:", lenght)

for i in list_sorted:
    print("posición:",list_sorted.index(i),", igual a:", i)
    if lenght%2==0: #si la longitud es par
        if list_sorted.index(i)==0:
            tuple_+= (i,)
            tuple_+= (list_sorted[list_sorted.index(i)+1],)
            new_list.append(tuple_)
            tuple_=tuple()
        elif list_sorted.index(i)%2==0 and list_sorted.index(i)!=1:
            tuple_+= (i,)
            tuple_+= (list_sorted[list_sorted.index(i)+1],)
            new_list.append(tuple_)
            tuple_=tuple()
    elif lenght%2!=0: #if length is odd, add the last item to a tuple together with the number `0`.
        if list_sorted.index(i)==0:
            tuple_+= (i,)
            tuple_+= (list_sorted[list_sorted.index(i)+1],)
            new_list.append(tuple_)
            tuple_=tuple()
        elif list_sorted.index(i)%2==0 and list_sorted.index(i)!=1 and list_sorted.index(i)+1!=lenght:
            tuple_+= (i,)
            tuple_+= (list_sorted[list_sorted.index(i)+1],)
            new_list.append(tuple_)
            tuple_=tuple()
        elif list_sorted.index(i)+1==lenght:
            tuple_+= (i,)
            tuple_+= (0,)
            new_list.append(tuple_)

print("List with tuples of two:", new_list)