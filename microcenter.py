from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time

def mc_scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    #creating the dictionary for the dataframe
    mc_listings = {'name':[], 'prices': []}
    #url for only the gpu's
    url = 'https://www.microcenter.com/category/4294966937/graphics-cards'

    browser.visit(url)

    for x in range(0,7):
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        names = soup.find_all('div',class_='pDescription compressedNormal2')
        prices = soup.find_all('div', class_='price')
    
        #grab the listing name
        for name in names:
            try:
                mc_listings['name'].append(name.text.strip())
            except:
                next
        #grab the price
        for price in prices:
            
            try:
                mc_listings['prices'].append(price.span.text)
            #some listings would not have a price and would raise an AttributeError, if it did then it would just give the price 0
            except AttributeError:
                mc_listings['prices'].append('0')
            
        #tag to move to the next page
        browser.find_by_text('>').first.click()
    browser.quit()
    return mc_listings