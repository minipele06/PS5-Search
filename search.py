import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "OOPS, please specify env var called 'TWILIO_ACCOUNT_SID'")
TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "OOPS, please specify env var called 'TWILIO_AUTH_TOKEN'")
SENDER_SMS  = os.environ.get("SENDER_SMS", "OOPS, please specify env var called 'SENDER_SMS'")
RECIPIENT_SMS  = os.environ.get("RECIPIENT_SMS", "OOPS, please specify env var called 'RECIPIENT_SMS'")

# AUTHENTICATE
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

URL = "https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815"
page = requests.get(URL,headers={"User-Agent":"Defined"})
soup = BeautifulSoup(page.content, "html.parser")
if soup.find(class_="prod-blitz-copy-message") is not None:
    print(soup.find(class_="prod-blitz-copy-message").get_text())
else:
    # COMPILE REQUEST PARAMETERS (PREPARE THE MESSAGE)
    content = "Hello, the PS5 is available at Walmart! https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815"
    message = client.messages.create(to=RECIPIENT_SMS, from_=SENDER_SMS, body=content)

URL = "https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161"
page = requests.get(URL,headers={"User-Agent":"Defined"})
soup = BeautifulSoup(page.content, "html.parser")
if soup.find(class_="btn btn-disabled btn-lg btn-block add-to-cart-button") is not None:
    print(soup.find(class_="btn btn-disabled btn-lg btn-block add-to-cart-button").get_text())
else:
    # COMPILE REQUEST PARAMETERS (PREPARE THE MESSAGE)
    content = "Hello, the PS5 is available at BestBuy! https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161"
    message = client.messages.create(to=RECIPIENT_SMS, from_=SENDER_SMS, body=content)

