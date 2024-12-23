import requests
import json

baseurl = 'http://localhost:12354/api/v1/Cubes(\'plan_BudgetPlan\')/Views(\'learnRESTAPIs\')/tm1.Execute?$expand=Cells'
auth = ('admin', 'apple')
headers = {"Content-Type" : "application/json"}
response = requests.post(baseurl, auth=auth, headers=headers)

data = response.json()
with open('cubeCellValue.json', 'w') as file:
    json.dump(data, file, indent=2)

#print(data)
