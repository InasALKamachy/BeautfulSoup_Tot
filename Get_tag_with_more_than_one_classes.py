import requests
from bs4 import BeautifulSoup
user_url = "https://ceng.cankaya.edu.tr/en/people/"

result = requests.get(user_url).text
soup = BeautifulSoup(result, 'html.parser')
#find = soup.find("h2")
#print(find.text)

find_class = soup.find_all('div', {'class':{'member_info', 'col-lg-5 col-md-12 col-sm-12'}})
for class_ in find_class:
    print(class_)
