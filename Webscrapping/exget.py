import requests
url="https://jsonplaceholder.typicode.com/posts/"
resp=requests.get(url)
print(resp.status_code)
print(resp.text)
