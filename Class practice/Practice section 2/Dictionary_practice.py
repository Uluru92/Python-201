my_description = {"name": "Jorddy", "lastName": "Castro", "Age": 32, "Country": "Costa_Rica",("New", "life", "Style"):"tup_1"}
print("My personal dictionary:", my_description)

my_description["Age"] = 20 # we can change the values, NOT NEVER EVER the key
print("Accesing the key Age and adding + 1 to it:",my_description["Age"]+1)

my_description["Color_eyes"] = "Blue" #we can add more keys with its own values: NEW ENTRY
print("My personal dictionary UPDATED:", my_description)

for key in my_description:
    print("show me the keys:", key)

for both in my_description.items():
    print("show me both key and values:", both)

for k in my_description.keys():
    print("show me the keys:",k)

for v in my_description.values():
    print("show me the values:",v)