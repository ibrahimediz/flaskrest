import requests
import json

apiurl = "https://jsonplaceholder.typicode.com/todos"
todo = {"userid":2,"title":"Ekmek Al","completed":False}
headers = {"Content-Type":"application/json"}
response = requests.post(apiurl,data=json.dumps(todo),headers=headers)

print(response.json())
print(response.status_code)