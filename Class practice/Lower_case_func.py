bucket_list = ["Go to Asia", "get a full body tattoo", "Have a Dalmata", "jump from the sky", "drink sea water"]
print("bucket list:",bucket_list) #full list

lowercase_bucket_list = [elements.lower() for elements in bucket_list]
print("lower case list #1:",lowercase_bucket_list) #full list in lower case

lowercase_bucket_list_2 = []
for elements in bucket_list:
    lowercase_bucket_list_2.append(elements.lower())
print("lower case list #2:",lowercase_bucket_list_2)


lowercase_bucket_list.sort() #order by alphabetics... if there is an Upper case, it goes first ... apparently
print("lower case list #1 sorted:",lowercase_bucket_list)

i_want_to = [f"I want to {x}" for x in lowercase_bucket_list]
print("I want to list:", i_want_to)