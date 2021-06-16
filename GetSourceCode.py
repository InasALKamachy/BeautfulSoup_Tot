import requests
from bs4 import BeautifulSoup
user_url = input("Enter Your URL bellow: ")

result = requests.get(user_url).text
print(result)
# put all source code of the page in new page and save it..
with open("new_page.html", "w", encoding="utf-8") as f:
    f.write(result)
    f.close()
