# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

#paréntesis... (entrega final de proyecto SQL en 8 días...)

def real_estate_adv(intro: str,*args)-> str:

    information = f"{intro}\n This is what this property offers:\n"

    return information