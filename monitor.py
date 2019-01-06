#created by Arya Hajikandi on 01/06/2019

import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

account_sid = 'your account sid'
auth_token = 'your auth token'
client = Client(account_sid, auth_token)

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

page = requests.get("https://www.barneys.com/product/canada-goose-macculloch-down-parka-505725823.html", headers=headers).text

soup = BeautifulSoup(page, "lxml")
element = soup.find("a", {"data-skuid":"00505057258287"})

if element.get("data-availabilitystatus") == "1000":
    message = client.messages \
                .create(
                     body="The product is currently in stock!",
                     from_='+twilio phone number you buy',
                     to='+your phone number'
                 )
else:
    pass