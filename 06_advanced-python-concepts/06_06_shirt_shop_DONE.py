# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]
gender = ["F","M"] #added my me just to check the tool futher... found out that you can combine 'n' with itertools.product!

#solution

import itertools

cartesian_product = list(itertools.product(colors,sizes,gender))

print(cartesian_product)