'''
Using the Chuck Norris API in combination with the datamuse API
( https://api.chucknorris.io/ - https://www.datamuse.com/api/ )

* Query the chucknorris api for a sentence
* Use the last word of that sentence to send a query to the Datamuse API
  and use the rel_rhy (or rel_nry) query parameter to fetch a word that rhymes
* Repeat a coupe of times and store the sentences and rhyme words
* Synthesize the collected results into an avant-garde poem and post on the forum ;)
'''
import requests
import string

poem_lines = []

while len(poem_lines) < 4:
    # Chuck Norris
    url_chuck = "https://api.chucknorris.io/jokes/random"
    response_chuck = requests.get(url_chuck)
    data_chuck = response_chuck.json()
    
    sentence = data_chuck['value']
    sentence_clean = sentence.strip(string.punctuation)
    last_word = sentence.split()[-1].strip(string.punctuation)

    # Datamuse
    url_datamuse = f"https://api.datamuse.com/words?rel_rhy={last_word}"
    response_datamuse = requests.get(url_datamuse)
    data_datamuse = response_datamuse.json()
    
    if not data_datamuse:
        continue # sometimes there is no rhyme...

    rhyme_word = data_datamuse[0]['word']
    poem_line = f"{sentence_clean} {rhyme_word}."
    poem_lines.append(poem_line)

poem = "\n\n".join(poem_lines)
print("\n--- avant-garde poem ---\n")
print(f"{poem}\n")

# Result avant-garde poem to post on the forum :)
'''
--- avant-garde poem ---

When Chuck Norris was born, his Dad celebrated by lighting up cigars, one for him and one for Chuck duck.

Chuck Norris' penis can make cold water shrink think.

After Chuck Norris ate a shrimp cocktail & a peanut butter sandwich, he won this year's Nobel Prize in Medicine for ridding the world of anaphylactic shock stock.

The City of Douche, NJ formally changed it's name to Hackensack after Chuck Norris spent a night in the local Motel 6 & simultaniously screwed 12 of the city's female taxi drivers divers.
'''