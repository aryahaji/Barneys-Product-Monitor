# Barneys Product Monitor

Sends a text message update to your phone if the product comes back in stock with info on how much stock is loaded. If the product isn't in stock it checks every 10 minutes to see if it is in stock.

Modifications needed
-------------------

- `account_sid` needs to be updated with your account_sid from twilio.
- `auth_token` needs to be updated with your auth_token from twilio.
- add url to product page on barneys.com to `page = requests.get(product url here)`.
- inspect element for size of product you want to monitor and look for `data_skuid`. Copy and paste that skuid into ` element = soup.find("a", {"data-skuid": "skuid here"})`.
- `from_` needs to be updated with your twilio phone number.
- `to` needs to be updated with your personal phone number or whatever phone number you want to recieve the texts.

> Optional: you can change how often you want the monitor to check to see if the product is in stock by changing the number in `time.sleep(600)`. NOTE: number is in seconds!

Possible issue
--------------

There could be an issue with _one size_ products as source code for _one size_ products are different and code doesn't account for that.

Installation
------------

- Install BeautifulSoup by running `pip install beautifulsoup4`
- Install requests by running `pip install requests`
- Install Twilio by running `pip install twilio`
- Install lxml by running `pip install lxml`
