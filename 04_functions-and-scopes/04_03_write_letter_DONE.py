# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def write_letter(name, text):
    """.
    Args:
        name (str): The name of the person you want to send a letter
        text (str): complete message
    Returns:
        str: A personalized letter
    """
    letter = print(f"\nDear {name},\n\n{text}\n\nBest wishes to you, {name}.\n")
    return

friend = "Jorddy"
words = "I hope this letter finds you well! Can you believe Christmas is just around the corner? I'm already getting into the holiday spirit, and I can't wait to celebrate with you. This year, let's make it extra special. How about a cozy gathering at my place with festive decorations, delicious food, and our favorite holiday movies? I'm thinking we could exchange gifts and maybe even bake some cookies together. Your presence always makes everything brighter. Looking forward to creating more wonderful memories with you this Christmas!"
write_letter(friend, words)