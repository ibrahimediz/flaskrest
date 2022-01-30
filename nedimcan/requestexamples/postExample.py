import requests, json

apiurl = "https://jsonplaceholder.typicode.com/todos"
todo = {"userid":5, "title":"Ekmek Al Unutma", "completed":False}
headers = {"Content-Type":"application/json"}

response = requests.post(apiurl, data=json.dumps(todo), headers=headers)
print(response.json())
print(response.status_code)
