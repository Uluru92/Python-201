def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

print_kwargs(country='ukraine', city='odessa')

# OUTPUT:
# country ukraine
# city odessa
