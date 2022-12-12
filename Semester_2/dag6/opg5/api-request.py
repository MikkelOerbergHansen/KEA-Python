import requests
import random

authors = ['Thomas', 'Mikkel', 'Signe', 'Cris', 'Sofie']

response = requests.post('http://127.0.0.1:5000/api/cluster', json={'author': random.choice(authors)})

if response.status_code == 200:
    print('Success!')
    print(response.content)
    print(response.text)
    print(response.json())
    print(response.json().keys())
    print(response.json()['author'])
    print(response.json()['type'])
    print(response.json()['url'])
elif response.status_code == 404:
    print('Not Found.')