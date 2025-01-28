'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "Fabian",
    "last_name": "Castro Araya",
    "email": "FabianJCA@gmail.com"
}

response = requests.post(base_url, json=body)

response = requests.get(base_url)

print(response.content)