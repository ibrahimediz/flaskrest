import requests
apiurl = "https://jsonplaceholder.typicode.com/todos/20"
response = requests.get(api_url)


todo ={ 'userId': 1, 'title': 'sucuklu yumurta yap', 'completed': False }
response = requests.put(api_url,json=todo)
print(response.json())
print(response.status_code)