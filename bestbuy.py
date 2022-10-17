from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time

def bb_scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    #creating the dictionary for the dataframe
    bb_listings = {'title':[], 'prices': []}
    #url for only the gpu's
    url = 'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002'

    browser.visit(url)

    for x in range(1,8):
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        results = soup.find_all('div', class_='priceView-hero-price priceView-customer-price')
        titles = soup.find_all('h4',class_='sku-title')
        
        #grab the price for each listing
        for result in results:
            price = result.span.text
            bb_listings['prices'].append(price)
        #some results have a different html tag for open box listings
        try:
            open_box = soup.find_all('span', class_='open-box-lowest-price')
            for open_box_result in open_box:
                price = open_box_result.text
                bb_listings['prices'].append(price)
        except:
            next
        #grab the listing name
        for title in titles:
            model_name = title.text.strip()
            bb_listings['title'].append(model_name)
            
        #the site is heavily css based so a text or href would not help
        browser.find_by_css('a.sku-list-page-next').first.click()

    browser.quit()
    
    return bb_listings

