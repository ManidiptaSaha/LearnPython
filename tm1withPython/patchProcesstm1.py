import requests
import json

myProcess = 'mover'
baseurl = 'http://localhost:12354/api/v1/'
endpoint = 'Processes(\''+ myProcess +'\')'
auth = ('admin','apple')

with open('processUpdated.json', 'r') as file:
     data = json.load(file)

'''
data = {
  "EpilogProcedure": "#****Begin: Generated Statements***\r\nCUBESETLOGCHANGES('plan_BudgetPlan', OldCubeLogChanges);\r\n#****End: Generated Statements****\r\nSaveDataAll();",
}

'''

response = requests.put(baseurl+endpoint, json=data, auth=auth)
print(response.json())
