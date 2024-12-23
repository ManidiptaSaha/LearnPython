import requests
import json

baseurl = 'https://car-fleet-management.herokuapp.com/cars'

def main_request(baseurl):
    r = requests.get(baseurl)
    r_json = json.loads(r.text)
    return r_json

json_data = main_request(baseurl)
print(json_data)

with open('carlist','w') as file:
   json.dump(json_data, file, indent=2)

