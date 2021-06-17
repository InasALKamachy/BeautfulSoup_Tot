import requests
from bs4 import BeautifulSoup

url="https://ceng.cankaya.edu.tr/en/people/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
collector = soup.find_all(class_="member_info")
for mail in collector:
    print(mail.text)
