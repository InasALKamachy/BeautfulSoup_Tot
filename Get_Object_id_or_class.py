import requests
from bs4 import BeautifulSoup
user_url = input("Enter Your URL bellow: ")
user_tag = input("Enter tag name: ")
serch_by = input("will you search by class or id ?")

if serch_by == 'id':
    user_id = input("Enter your id: ")
    result = requests.get(user_url).text
    soup = BeautifulSoup(result, 'html.parser')
    find = soup.find(user_tag, id=user_id)
    print(find)
elif serch_by =='class':
    user_class = input("Enter user class: ")
    result = requests.get(user_url).text
    soup = BeautifulSoup(result, 'html.parser')
    find = soup.find_all(user_tag, class_=user_class)
    print(find)






