#Enumerate function
siblings = ["Maritza","Melvin","Mirna","Maribel","Sandra","Yadira","Javier","Dixie"]
for index, person in enumerate(siblings, start=1):
    print(f"Sibling #{index}: {person}")

    
#Alternative
courses = ["Maritza","Melvin","Mirna","Maribel","Sandra","Yadira","Javier","Dixie"]
for index in range(len(courses)):
    print(f"Sibling #{index+1}: {courses[index]}")