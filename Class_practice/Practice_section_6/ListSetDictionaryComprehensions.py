listcomp = [x*2 for x in range(5)]
setcomp = {x*2 for x in range(5)}

dict_1 = {"a": 1, "b": 8}
dict_2 = {k: v*2 for (k, v) in {"a": 1, "b": 8}.items()}

print(listcomp)
print(setcomp)
print(dict_1)
print(dict_2)