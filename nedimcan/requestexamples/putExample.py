import requests, json

apiurl = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(apiurl)
todo = {"userid":1, "title":"Ekmek Almadim ama Kola ve Cips aldim", "completed":True, "id":10}
# headers = {"Content-Type":"application/json"}

response = requests.put(apiurl, data=json.dumps(todo))
print(response.json())
print(response.status_code)

response = requests.get(apiurl)
print(response.json())