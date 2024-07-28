#Enumerate function
print("Using enumerate function: ")
siblings = ["Maritza","Melvin","Mirna","Maribel","Sandra","Yadira","Javier","Dixie"]
for index, person in enumerate(siblings, start=1):
    print(f"Sibling #{index}: {person}")

    
#Alternative
print("Alternative way to do it: ")
for index in range(len(siblings)):
    print(f"Sibling #{index+1}: {siblings[index]}")

print("Just enumerate a list: ")
siblings_list = list(enumerate(siblings))
print(siblings_list)    