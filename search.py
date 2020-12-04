import requests
from bs4 import BeautifulSoup

URL = "https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815"
page = requests.get(URL,headers={"User-Agent":"Defined"})
soup = BeautifulSoup(page.content, "html.parser")
if soup.find(class_="prod-blitz-copy-message") is not None:
    print(soup.find(class_="prod-blitz-copy-message").get_text())
else:
    print("Product is Available")

