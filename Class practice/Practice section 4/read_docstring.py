def greet(greeting: str, name: str) -> str:
    """Generates a greeting.

    Args:
        greeting (str): The greeting to use, e.g., "Hello"
        name (str): The name of the person you want to greet

    Returns:
        str: A personalized greeting message
    """

    sentence = f"{greeting}, {name}! How are you?"
    return sentence

#help(): you can pass the function object as an argument to help()
#.__doc__: you can access the __doc__ attribute of greet

print(greet.__doc__)