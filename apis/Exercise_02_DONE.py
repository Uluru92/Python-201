'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(base_url)

emails_list = []

data = response.json()["data"] 

for user in data:
    emails_list.append('User: '+ user["first_name"]+' / Email: '+user["email"])

pprint(emails_list)