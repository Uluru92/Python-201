# Something is wrong with the way you're calling the function below.
# Can you fix it and survive?

def skydive(step_1, step_2):
    print("For your own safety, please follow the instructions carefully:")
    print(f"1. {step_2}") #step_2 is the FIRST STEP! 
    print(f"2. {step_1}") #now... you can JUMP!

skydive("JUMP!", "Take your parachute.")

#OR... RE ORDER YOUR ARGUMENTS!

def skydive(step_1, step_2):
    print("For your own safety, please follow the instructions carefully:")
    print(f"1. {step_1}") #step_2 is the FIRST STEP! 
    print(f"2. {step_2}") #now... you can JUMP!

skydive("Take your parachute.", "JUMP!") 