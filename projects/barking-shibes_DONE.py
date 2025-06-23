# Use a quotes API, e.g. https://api.quotable.io/quotes/random
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://en.wikipedia.org/wiki/Doge_(meme))
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.

###################
##               ## 
##   SOLUTION:   ##
##               ## 
###################

# I used the following API for my quotes: https://api.kanye.rest
# I used the following API for my images: https://api.thecatapi.com/v1/images/search

from pathlib import Path
import requests
import webbrowser

quotes_api_url = 'https://api.kanye.rest' 
quotes_response = requests.get(quotes_api_url)

if quotes_response.status_code == 200:
    ninja_info = quotes_response.json()
else:
    print("Error:", quotes_response.status_code, quotes_response.text)

images_api_url = 'https://api.thecatapi.com/v1/images/search'
images_response = requests.get(images_api_url)

if images_response.status_code == 200:
    cats_info = images_response.json()
else:
    print("Error:", images_response.status_code, images_response.text)

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Barking-shibes-exercise</title>
    <style>
        body {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-family: Arial, sans-serif;
            min-height: 100vh;
            margin: 0;
            padding: 2rem;
            background-color: #f9f9f9;
            text-align: center;
        }}
        .quote {{
            font-size: 1.5rem;
            font-style: italic;
            margin-bottom: 2rem;
            max-width: 700px;
        }}
        img {{
            max-width: 80%;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body>
    <div class="quote">"{ninja_info['quote']}"</div>
    <img src="{cats_info[0]['url']}" alt="Gato">
</body>
</html>
"""

f = Path(r"C:\Users\jordd\Documents\Repositorios Github\Python-201\projects\cats_quotes.html")
f.write_text(html_content)

webbrowser.open(f"file://{f}")

