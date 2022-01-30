# GET

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()

# POST 
import json
apiurl = "https://jsonplaceholder.typicode.com/todos"
todo = {"userid":2,"title":"Ekmek Al","completed":False}
headers = {"Content-Type":"application/json"}
response = requests.post(apiurl,data=json.dumps(todo),headers=headers)
print(response.json())
print(response.status_code)

# PUT

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

todo = {'userId': 1, 'id':10, 'title': 'İKİ EKMEK', 'completed': False}
response = requests.put(api_url,json=todo)
print(response.json())
print(response.status_code)


response = requests.get(api_url)
print(response.json())