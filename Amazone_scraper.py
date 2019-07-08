#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:48:15 2019

@author: stableaf_

@Pre-requistes: Installed libraries, Proper User-agent for browser handling, Goggle genereated password
"""



# Importing required Libraries 
import requests
from bs4 import BeautifulSoup
import smtplib

# Assigning Product URL and User-agent browser to variables
URL = "https://www.amazon.in/Intel-16-Thread-BX80684I99900K-Processor-Graphics/dp/B005404P9I/ref=sr_1_1?crid=SWGRV6JNTFOH&keywords=i9+9900k&qid=1562599894&s=gateway&sprefix=i9+%2Caps%2C350&sr=8-1"
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}


# Fucntion to check detect change
def check_price_change():
    page = requests.get(URL, headers = headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    get_product = soup.find(id="productTitle").get_text()
    print("\n\n\nProduct: ", get_product.strip())
    
    # Extracting Price from the Main page    
    get_raw_price = soup.find(id="priceblock_ourprice").get_text()
    print("\n\n\nPrice: ",get_raw_price.strip())
    
    if get_raw_price.strip() != '₹ 44,250.00':
        notify()
 
# Function to send the notification Email       
def notify():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('hrugvedghait4@gmail.com', 'yckubfcsgffjvgfn')
    
    subject = 'Price of the camera has changed.'
    body = 'Check out the link: https://www.amazon.in/Intel-16-Thread-BX80684I99900K-Processor-Graphics/dp/B005404P9I/ref=sr_1_1?crid=SWGRV6JNTFOH&keywords=i9+9900k&qid=1562599894&s=gateway&sprefix=i9+%2Caps%2C350&sr=8-1'
    
    message = f"Subject: {subject} \n\n {body}"
    
    server.sendmail('hrugvedghait4@gmail.com', 'hrugvedghait5@gmail.com' , message)
    
    print("\n\n\nOperation Successful!! Email has been sent. \n\n")
    
    server.quit()
    
# Calling function
check_price_change()