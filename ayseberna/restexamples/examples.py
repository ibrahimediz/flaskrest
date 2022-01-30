import requests
import json

###### post example
apiurl = "https://jsonplaceholder.typicode.com/todos"

todo = {"userid":2,"title":"Ekmek Al","completed":False}
headers = {"Content-Type":"application/json"}
response = requests.post(apiurl,data=json.dumps(todo),headers=headers)
print(response.json())
print(response.status_code)


###### put example, update

apiurl = "https://jsonplaceholder.typicode.com/todos/10"
todo = {'userId': 1, 'id': 10, 'title': 'Iki ekmek yarim kalip beyaz peynir', 'completed': False}

response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)

