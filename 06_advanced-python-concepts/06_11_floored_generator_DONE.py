# Adapt your Generator expression from the previous exercise:
# Add a floor division by 1111 on it.
# What numbers do you get?

#solution...

nums = (x/1111 for x in range(1, 10000))
for x in nums:
    print(x*1111, "->", x)
