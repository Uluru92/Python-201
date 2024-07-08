# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.
def greet(greetings, name):
    sentence = f"\n{greetings}, {name}! How are you?\n\n"
    return sentence

def write_letter(name, text):
    """.
    Args:
        name (str): The name of the person you want to send a letter
        text (str): complete message
    Returns:
        str: A personalized letter
    """
    greeting = greet(greetings, name)
    letter = print(f"{greeting}{text}\n\nBest wishes to you, {name}.\n") 
    return

greetings = "Hey you!"
friend = "Jorddy"
words = "I hope this letter finds you well! Can you believe Christmas is just around the corner? I'm already getting into the holiday spirit, and I can't wait to celebrate with you. This year, let's make it extra special. How about a cozy gathering at my place with festive decorations, delicious food, and our favorite holiday movies? I'm thinking we could exchange gifts and maybe even bake some cookies together. Your presence always makes everything brighter. Looking forward to creating more wonderful memories with you this Christmas!"
write_letter(friend, words)