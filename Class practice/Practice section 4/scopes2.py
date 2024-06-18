name = "Name1"
def print_name_box():
    global name
    print(name)
    name = "Name2"
    def smaller_box():
        name = "Name3"
        print(name)
        def smallest_box():
            name = "Name333"
            print(name)
        smallest_box()
    smaller_box()
print_name_box()