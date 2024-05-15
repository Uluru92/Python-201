bucket_list = ["Go to Asia", "get a full body tattoo", "Have a Dalmata", "jump from the sky", "Allow someone in"]
print("bucket list:",bucket_list) #full list

lowercase_bucket_list = [elements.lower() for elements in bucket_list]
print("bucket list in lower case:",lowercase_bucket_list) #full list in lower case

lowercase_bucket_list.sort() #order by alphabetics... if there is an Upper case, it goes first ... apparently
print(lowercase_bucket_list)

print(bucket_list[1:2]) #returns the space 1 to the 2

bucket_list.pop(0) #eliminates the first space
print(bucket_list)

bucket_list.append("ride a tiger") #add an element to the list
print(bucket_list)

next_task = bucket_list.pop() #removes an element and at the same time assign it to a variable
print("next_task: "+next_task)

bucket_list.remove("jump from the sky") #remove an element 
print(bucket_list)

bucket_list.remove(bucket_list[0]) #remove an elemment using indexing to access the value
print(bucket_list)

bucket_list.insert(1, "have 3 cats")
print(bucket_list)



a = [1,2,3]
b = [1,2,3]
print(a,b)
print(type(a))  

a[0] = 123
print(a,b)

c = a
c[0] = 999
print(a,b)