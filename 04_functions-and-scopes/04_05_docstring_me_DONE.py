# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """
    Translates a given Spanish word to English.

    Args:
        km (int): The distance in kilometers.

    Returns:
        miles (int): The distance in miles.

    Example:
        >>> km_to_miles(15)
        9.0
    """
    miles = km * 0.6
    print(miles) #added just to get some output!
    return miles

print(km_to_miles.__doc__)
km_to_miles(15)
