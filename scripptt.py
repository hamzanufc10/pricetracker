import requests
import smtplib
from bs4 import BeautifulSoup


#whichever item you are planning to buy
URL='https://www.amazon.in/Nivia-Storm-Football-Size-White/dp/B00ICCYF0E/ref=sr_1_1?dchild=1&keywords=fotball&qid=1569670655&sr=8-1'


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


def check_price():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id='productTitle').get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    converted_price=float(price[2:5])

    if(converted_price < 329.0):
        send_mail()

        print(title.strip())
        print(converted_price)



def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #use 2-way authentication and genrete a password 
    server.login('qwerty@gmail.com','pa2dsasr432fsa33f32word123fsa324')

    subject='Hey!price fell down!'
    body='check the amzon link :https://www.amazon.in/Scotch-Brite-Bathroom-scrubber-brush-Green/dp/B00NBM24PS/ref=sr_1_13?keywords=brush&qid=1569183573&sr=8-13'
    msg=f'Subject:{subject}\n\n{body}'


    server.sendmail(
        'qwerty@gmail.com',
        'zltan.9595@gmail.com',
        msg
    )
    print('hey! email has been sent')

    server.quit()


check_price()
