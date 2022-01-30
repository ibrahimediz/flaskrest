import requests, json

apiurl = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(apiurl)
todo = {"title":"Ekmek Yok Cips Al"}
# headers = {"Content-Type":"application/json"}

response = requests.patch(apiurl, json=todo)
print(response.json())
print(response.status_code)

response = requests.get(apiurl)
print(response.json())