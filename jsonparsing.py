import requests
import json

'''
use json.load to load from a file
use json.loads to load a string
use json.dump to dump in a file
use json.dumps to dump as a string
'''

response = requests.get('https://car-fleet-management.herokuapp.com/cars')
response_json = json.loads(response.text)
print(json.dumps(response_json,indent = 2))


'''
with open('response.json') as file:
    data = json.load(file)

for i in data:
    del i['build']

with open('myexport','w') as export:
    json.dump(data, export, indent=2)

'''
