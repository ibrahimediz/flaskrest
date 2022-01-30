import requests
api_url = "https://jsonplaceholder.typicode.com/todos/20"
response = requests.get(api_url)
print(response.json())

todo = {'userId':1,'title':'ekmek peynir','completed':False }
response = requests.put(api_url,json=todo)
print(response.json())