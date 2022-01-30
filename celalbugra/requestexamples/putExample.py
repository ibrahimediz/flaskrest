import requests
api_url = "https://jsonplaceholder.typicode.com/todos/19"
response = requests.get(api_url)
print(response.json())

todo = {'userId':1,'title':'iki ekmek yarım kalıp beyaz peynir','completed':False}
response = requests.put(api_url,json=todo)
print(response.json())
print(response.status_code)

response = requests.get(api_url)
print(response.json())