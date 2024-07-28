def my_enumerate(sequence):
    index = 0
    for item in sequence:
        yield index, item
        index += 1

courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']

for index, course in my_enumerate(courses):
    print(f"{index}: {course} Python")

# OUTPUT:
# 0: Intro Python
# 1: Intermediate Python
# 2: Advanced Python
# 3: Professional Python