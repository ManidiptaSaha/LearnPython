import requests
import json

baseurl = 'https://car-fleet-management.herokuapp.com/cars'

data = {"manufacturer": "Tata", "model": "Nexon.Ev", "build": 2001}

#if response.post doesn't include json=<data> we need to add headers = {"Content-Type":"application/json"
#convert data in json string using data = json.dumps(<data>)
#see the construction below
headers = {"Content-Type":"application/json"}
response = requests.post(baseurl, data=json.dumps(data), headers=headers)


#else we may use the following construction of request
'''
response = requests.post(baseurl, json=data)
'''


print(response.json())


