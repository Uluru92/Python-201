generator = (x*2 for x in range(5))

print(generator)  
# OUTPUT: <generator object <genexpr> at 0x1106845f0>

print(type(generator))  
# OUTPUT: <class 'generator'>

gen = (x*2 for x in range(5))
for i in gen:
    print(i)

# OUTPUT:
# 0
# 2
# 4
# 6
# 8