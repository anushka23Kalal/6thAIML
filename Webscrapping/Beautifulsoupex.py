from bs4 import BeautifulSoup
with open(r"C:\Users\HP\Desktop\6thsem_AIML\Module 3\index.html","r") as file:
    content=file.read()
soup=BeautifulSoup(content,"html.parser")
# print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.find("a"))
print(soup.find_all("a"))
