import requests
import json

baseurl = 'http://localhost:12354/api/v1/'
endpoint = 'Processes'
auth = ('admin','apple')

with open('postProcess.json', 'r') as file:
     data = json.load(file)

response = requests.post(baseurl+endpoint, json=data, auth=auth)
print(response.json())

