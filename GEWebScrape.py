#Module Name: GEWebScrape
#Imported by insert_data
#used to scrape price data from Giant Eagle
#Team Members: Bryce Benjamin, Cliff Rosenberg, Jordan Christan, Aarush Gupta

import requests
import sys
import numpy as np 
from urllib.request import urlopen
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
#from selenium.webdriver import Edge
from selenium.webdriver.common.by import By

#group the urls for the recipes on Giant Eagle
tacoURLs = ("https://shop.gianteagle.com/waterworks/search/product/00000000040617",
"https://shop.gianteagle.com/waterworks/search/product/00030034007737",
"https://shop.gianteagle.com/waterworks/search/product/00201688000003",
"https://shop.gianteagle.com/waterworks/search/product/00064144282432",
"https://shop.gianteagle.com/waterworks/search/product/00046000811017",
"https://shop.gianteagle.com/waterworks/search/product/00073420000110")

spaghettiURLs = ("https://shop.gianteagle.com/waterworks/search/product/00030034045890",
"https://shop.gianteagle.com/waterworks/search/product/00074908324414",
"https://shop.gianteagle.com/waterworks/search/product/00030034038618",
"https://shop.gianteagle.com/waterworks/search/product/00030034007751")

burgerURLs = ("https://shop.gianteagle.com/waterworks/search/product/00030034400453",
"https://shop.gianteagle.com/waterworks/search/product/00201688000003",
"https://shop.gianteagle.com/waterworks/search/product/00048001213487",
"https://shop.gianteagle.com/waterworks/search/product/00000000040617",
"https://shop.gianteagle.com/waterworks/search/product/00000000041614",
"https://shop.gianteagle.com/waterworks/search/product/00054100000606",
"https://shop.gianteagle.com/waterworks/search/product/00013120014611",
"https://shop.gianteagle.com/waterworks/search/product/00013000626095")

tunaFishURLS = ("https://shop.gianteagle.com/waterworks/search/product/00072945601369",
"https://shop.gianteagle.com/waterworks/search/product/00048001213487",
"https://shop.gianteagle.com/waterworks/search/product/00080000006721",
"https://shop.gianteagle.com/waterworks/search/product/00054100000606")

pancakeURLS = ("https://shop.gianteagle.com/waterworks/search/product/00030034004644",
"https://shop.gianteagle.com/waterworks/search/product/00030000059708",
"https://shop.gianteagle.com/waterworks/search/product/00030034000509")

omeletteURLS = ("https://shop.gianteagle.com/waterworks/search/product/00000000048002",
"https://shop.gianteagle.com/waterworks/search/product/00000000041614",
"https://shop.gianteagle.com/waterworks/search/product/00030034000509",
"https://shop.gianteagle.com/waterworks/search/product/00030034302047",
"https://shop.gianteagle.com/waterworks/search/product/00030034007737")


def getPrices(recipe):
    '''
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    self.driver = webdriver.Chrome('C:/chromedriver.exe')
    driver = self.driver
    '''
    driver = webdriver.Chrome('C:/chromedriver.exe')

    if recipe == "taco":
        recipeURLS = tacoURLs
    elif recipe == "spaghetti":
        recipeURLS = spaghettiURLs
    elif recipe == "burger":
        recipeURLS = burgerURLs
    elif recipe == "tuna":
        recipeURLS = tunaFishURLS
    elif recipe == "pancake":
        recipeURLS = pancakeURLS
    elif recipe == "omelette":
        recipeURLS = omeletteURLS

    set_of_item_prices = set()
    for url in recipeURLS:
        #retrieving the pages from giant eagle 
        driver.get(url)
        div_element = driver.find_element(By.TAG_NAME, 'div')
        #printing the food name
        food_name = div_element.find_element(By.CLASS_NAME, 'ProductDetailMainCard_title')
        #for e in food_name:

        #getting the main price div section on the webpage
        price = div_element.find_element(By.CLASS_NAME, 'ProductDetailMainCard_price')
        
        #if there is a discount price on the page, then print that. If no discount price then just print the main price
        try:
            compared_price = price.find_element(By.CLASS_NAME, 'SharedProductPricingDetails_comparedPrice')
            tabular = compared_price.find_element(By.CLASS_NAME, 'tabular')
            tup = (food_name.text, tabular.text)
            set_of_item_prices.add(tup)
        except:
            lh_solid = price.find_element(By.CLASS_NAME, 'lh-solid')
            new_lh_solid_list = lh_solid.text.split('\n')
            #if len(new_lh_solid_list) == 1, then no need to concatenate the string back together. if len == 2, then we have to concatenate the string back together.
            if len(new_lh_solid_list) == 1:
                price_of_item = new_lh_solid_list[0]
            else:
                price_of_item = new_lh_solid_list[0] + '.' + new_lh_solid_list[1]
            
            #store name and price as tuple in the set
            tup = (food_name.text, price_of_item)
            set_of_item_prices.add(tup)

    #return the set 
    return(set_of_item_prices)