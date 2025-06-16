'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 12008,
    "email": "Luisano@hotmail.com",
    "first_name": "Luis",
    "last_name": "Herrero Fonseca",
    "created_at": 1750104729000,
    "updated_at": 1750104729000
}

response = requests.post(base_url, json=body)

response = requests.get(base_url)

print(response.content)