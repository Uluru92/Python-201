name = "Mycroft"
def print_name_box():
    name = "Carlos"
    print(name)
    def smaller_box():
        # (Re)assigning a variable within a local scope
        # overwrites the same variable from an outer scope
        # You also can't use the global variable *before*
        # assigning it, if you assign it anywhere in that scope.
        # --TASK--: uncomment the print() function below
        #    and interpret the results when running the script
        name = "Delfina"
        print(name)
        name = "Luca"
        print(name)
        def smallest_box():
            # Inner scopes always draw from the next outer layer.
            # After `name` got overwritten, the name that will
            # be printed is NOT the global-scope name anymore
            name = "Jorddy"
            print(name)
            name = "Mycroft"   
            print(name)         
        smallest_box()
    smaller_box()
print_name_box()

name = "Prueba1"

def print_name_box():
    print(name)
    def smaller_box():
        name = "Prueba2"
        print(name)

        def smallest_box():
            name = "Prueba3"
            print(name)

        smallest_box()

    smaller_box()

print_name_box()