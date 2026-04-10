import requests
from bs4 import BeautifulSoup
url="http://quotes.toscrape.com"
resp=requests.get(url)
soup=BeautifulSoup(resp.text,"html.parser")
quotes=soup.findAll("div",class_="quote")
# print(soup.find("a"))
# print(soup.findAll("a"))
for q in quotes:
    text = q.find("span", class_="text").text
    author = q.find("small", class_="author").text
    tag = q.find("a", class_="tag").text
print(text)
print(author)
print(tag)
print("------")
