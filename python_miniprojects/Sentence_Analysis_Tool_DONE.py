#Write a script that takes a sentence from the user and returns:
#the number of lower case letters
#the number of uppercase letters
#the number of punctuations characters
#the total number of characters
#Use a dictionary to store the count of each of the above.
#Note: ignore all spaces.
#Example input: I love to work with dictionaries!
#Example output:
#Upper case: 1
#Lower case: 26
#Punctuation: 1
#Total chars: 28

script = input("Write some text: ")

counter_upper_case = 0
counter_lower_case = 0
counter_punctuation = 0
counter_total_chars = 0

for i in script:
    if i in "abcdefghijklmnopqrstuvwxyz":
        counter_lower_case = counter_lower_case + 1
    elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        counter_upper_case = counter_upper_case + 1
    elif i == "!"or i =="¿"or i =="?"or i =="!"or i =="…"or i =="¡"or i ==":"or i ==";"or i =="("or i ==")"or i =="["or i =="]"or i =="{"or i =="}"or i ==",":#and i !=" ":
        counter_punctuation = counter_punctuation + 1
        
counter_total_chars = counter_lower_case + counter_punctuation + counter_upper_case

print("Upper case:", counter_upper_case)
print("Lower case:", counter_lower_case)
print("Punctuation:", counter_punctuation)
print("Total chars:", counter_total_chars)