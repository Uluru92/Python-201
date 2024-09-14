# Adapt your Generator expression from the previous exercise:
# Add a floor division by 1111 on it.
# What numbers do you get?

#solution...
#honestly i did not understand the question itself...  what does it mean to ''add a floor division by 1111 on it''...?
#that's exactly what the generator already does... to find out the numbers divisibles by 1111.

nums = (x for x in range(1, 1000000))
for x in nums:
    if x%1111 == 0:
        print(x)