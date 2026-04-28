import requests
url="https://jsonplaceholder.typicode.com/posts/"
data = {
    "title": "AI ML Class",
    "body": "Learning Web Scraping",
    "userId": 1
}
resp=requests.post(url,json=data)
print(resp.status_code)
print(resp.json())
