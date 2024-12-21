import requests
import pandas as pd

baseUrl = 'https://rickandmortyapi.com/api/'
endpoint = 'character/'

def main_request(baseUrl, endpoint, x):
    r = requests.get(baseUrl + endpoint + f'?page={x}')
    return r.json()

def get_pages(response):
    return(response['info']['pages'])

def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {
        'id' : item['id'],
        'name' : item['name'],
        'no_ep' : len(item['episode']),
        }
        charlist.append(char)
    return charlist

data = main_request(baseUrl, endpoint, 1)

mainlist = []
for x in range(1, get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(baseUrl, endpoint, x)))

df = pd.DataFrame(mainlist)
df.to_csv('characterlist.csv',index=False)

