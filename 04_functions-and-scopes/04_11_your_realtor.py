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
        details += detail + "\ln"
    
    information = ""
    information = f"{intro}\n This is what this property {property_name} offers:\n"+details
    print(information)

