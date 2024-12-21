import requests
import json
import pandas as pd

baseurl = 'http://localhost:12354/api/v1/'
endpoint = 'Cubes'
auth = ('admin','apple')

def main_request(baseurl, endpoint):
    r = requests.get(baseurl + endpoint, auth=auth)
    return r.json()

def get_cube_no(response):
    return len(response['value'])

def get_rule(response, x):
    rule = response['value'][x]['Rules']
    return rule


response = main_request(baseurl, endpoint)

rule = []
for item in range(0,1,1):
    rule_lines = get_rule(response, item)
    rule.append(rule_lines)

print(rule)

with open('PlanSamp_rule.txt', 'w') as file:
    for i in rule:
        file.write(i + '\n')