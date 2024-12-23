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

def get_cube_name(response, x):
    cube = response['value'][x]['Name']
    return cube


response = main_request(baseurl, endpoint)
tot_cubes = get_cube_no(response)

cubelist = []
for item in range(tot_cubes):
    cube_name = get_cube_name(response, item)
    cubelist.append(cube_name)

print(cubelist)

df = pd.DataFrame(cubelist)
#to ignore pandas indexing use index = False
df.to_csv('PlanSamp_cubelist.csv', index=False)

with open('PlanSamp_cubelist.txt', 'w') as file:
    for i in cubelist:
        file.write(i + '\n')