# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

#paréntesis... (entrega final de proyecto SQL en 8 días...)

def real_estate_adv(intro: str, property_name: str, *args)-> str:

    """Prints out nicely formatted information about a real estate advertisement.
    Args:
        intro (str): The text to use as an introduction to the property description
        property_name (str): The name of the property
        *args: details about the property
    """
    details = ""
    for detail in args:
        details += "* "+detail+"\n"
    
    information = ""
    information = f"{intro}\nProperty name: {property_name}\nThis is what offers:\n"+details
    print(information)

real_estate_adv("The most beautiful property you could get this next year!!","SUMMER HOUSE","2000 square meters","1 Master Room","3 Secondary Rooms","4 Bathdrooms","1 Kitchen","2 Living Rooms","2 Gardens","3 Floors","Sunset View","Indoor and Outdoor Pool")

