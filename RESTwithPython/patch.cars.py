import requests
import json

baseurl = 'https://car-fleet-management.herokuapp.com/cars/5'

response = requests.get(baseurl)
print(response.json())

'''
IN PATCH you need to ONLY provide the key and updated value pairs unlike PUT
'''
#oldData
#data = {"manufacturer": "Tata", "model": "Nexon", "build": 2001}

#newData for PUT
data = {"build": 2002}

#headers = {"Content-Type":"application/json"}
#response = requests.post(baseurl + endpoint, data=json.dumps(data), headers=headers)
#response.json()

#PATCH NOT SUPPORTED for this API
response = requests.patch(baseurl, json=data)
print(response.json())


