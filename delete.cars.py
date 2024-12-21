import requests
import json

baseurl = 'https://car-fleet-management.herokuapp.com/cars/8'

response = requests.get(baseurl)
print(response.json())

response = requests.delete(baseurl)
print(response.json())



