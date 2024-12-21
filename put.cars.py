import requests
import json

baseurl = 'https://car-fleet-management.herokuapp.com/cars'

response = requests.get(baseurl)
print(response.json())

#oldData
#data = {"manufacturer": "Tata", "model": "Nexon", "build": 2000}

#newData for PUT
data = {"id" : 5, "manufacturer": "Tata", "model": "Nexon", "build": 2001}

#headers = {"Content-Type":"application/json"}
#response = requests.post(baseurl + endpoint, data=json.dumps(data), headers=headers)
#response.json()

response = requests.put(baseurl, json=data)
print(response.json())


