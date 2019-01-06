# created by Arya Hajikandi on 01/06/2019

import requests
import time
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from twilio.rest import Client

load_dotenv()

while True:
    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("auth_token")
    client = Client(account_sid, auth_token)

    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    }

    page = requests.get(
        "https://www.barneys.com/product/canada-goose-macculloch-down-parka-505725823.html",
        headers=headers,
    ).text

    soup = BeautifulSoup(page, "lxml")
    element = soup.find("a", {"data-skuid": "00505057258287"})
    quantity = element.get("data-onhand-quantity")

    if element.get("data-availabilitystatus") == "1000":
        message = client.messages.create(
            body="The product is currently in stock! There is/are "
            + quantity
            + " in stock.",
            from_=os.getenv("from_"),
            to=os.getenv("to"),
        )
    else:
        pass
    time.sleep(600)