import requests
from bs4 import BeautifulSoup
user_url = input("Enter Your URL bellow: ")

result = requests.get(user_url).text
soup = BeautifulSoup(result, 'html.parser')
#find = soup.find("h2")
#print(find.text)
find_header = soup.find_all(['h1','h2','h3','h4','h5','h6'])
for header in find_header:
    print(header)
