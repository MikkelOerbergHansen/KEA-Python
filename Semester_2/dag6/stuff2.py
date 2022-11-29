
import requests
import json



def elspotpriser():
   
    url = 'http://127.0.0.1:5000/api/data'
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers).json()
    
    return response





data = elspotpriser()
print(data)







