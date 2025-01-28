import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(base_url)

print(response.status_code)
print(response.encoding)
pprint(response.text)
