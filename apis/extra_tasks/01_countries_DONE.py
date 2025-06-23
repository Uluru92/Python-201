'''
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals
'''

import requests
from pprint import pprint

base_url = "https://restcountries.com/v3.1/name/"

response = requests.get("https://restcountries.com/v3.1/name/costa")

if response.status_code == 200:
    tasks = response.json()
    country_name = tasks[0]["name"]["common"]  
    population_CR = tasks[0]["population"]
    area_cr = tasks[0]["area"]
    native_name = tasks[0]["name"]["nativeName"]["spa"]["official"]
    capital = tasks[0]["capital"][0]
    print(f"\nMy home country is {country_name}.\nNative name: {native_name}. \nPopulation: {population_CR} people. \nCapital: {capital}.")
else:
    print("Failed to fetch country details")

response = requests.get("https://restcountries.com/v3.1/name/chile")

if response.status_code == 200:
    tasks = response.json()
   
    country_name = tasks[0]["name"]["common"] 
    population_Chile = tasks[0]["population"]
    area_chile = tasks[0]["area"]
    native_name = tasks[0]["name"]["nativeName"]["spa"]["official"]
    capital = tasks[0]["capital"][0]

    print(f"\nMy actual country is {country_name}.\nNative name: {native_name}. \nPopulation: {population_CR} people. \nCapital: {capital}.")

else:
    print("Failed to fetch country details")

print(f"\nCosta Rica has {area_cr} km2 and Chile has {area_chile} km2, they differ in {area_chile-area_cr} km2\n")
