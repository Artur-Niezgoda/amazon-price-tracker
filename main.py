import requests
from bs4 import BeautifulSoup
from notification_manager import NotificationManager

# Put price limit and a link to the item you are interested in
mng = NotificationManager()
price_limit = 15
URL = "https://a.co/d/5iUKt2H"

header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/107.0.0.0 Safari/537.36"
}

response = requests.get(url=URL, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
price = float(soup.find("span", class_=["a-offscreen"]).get_text().split("$")[1])
name = " ".join(soup.find(id="productTitle").getText().split())

if price < price_limit:
    mng.send_email(f"The price of {name} dropped below {price_limit} and is now {price}")