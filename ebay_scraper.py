import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.ebay.com/itm/Aluminium-HD-Polarized-Photochromic-Sunglasses-Men-Chameleon-Driving-Sun-Glasses/254204493465'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify())

    title = soup.find(id="itemTitle").get_text()
    price = soup.find(id="prcIsum").get_text()[1:].strip().replace(',','')
    converted_price = float(price)
    print(converted_price)
    print(title.strip())

    if(converted_price < 1.700):
        send_mail()

def send_mail():
    server = smtplib.SMPT('smpt.gmail.com', 587)
    server.ehlo()
    server.startls()
    server.ehlo
    
    server.login('prabin.b9@gmail.com','googleAppCodeGoesHere')

    subject = 'Hey, Price of the product fell down'
    body = 'Check an eBay Link https://www.ebay.com/itm/Aluminium-HD-Polarized-Photochromic-Sunglasses-Men-Chameleon-Driving-Sun-Glasses/254204493465'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail('prabin.b9@gmail.com','prabinparajuli10@gmail.com',msg)
    print('Email Has been Sent!')

    server.quit()

check_price()
