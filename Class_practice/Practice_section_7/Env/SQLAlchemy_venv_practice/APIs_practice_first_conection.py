import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "Jorddy",
    "last_name": "Castro Araya",
    "email": "jorddy.castro@gmail.com"
}

response = requests.post(base_url, json=body)