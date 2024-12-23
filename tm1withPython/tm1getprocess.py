import requests
import json

myProcess = 'mover'
baseurl = 'http://localhost:12354/api/v1/'
endpoint = 'Processes(\''+ myProcess +'\')'
auth = ('admin','apple')
response = requests.get(baseurl + endpoint, auth=auth)

data = response.json()

with open('process.json', 'w') as file:
    json.dump(data, file, indent=2)
