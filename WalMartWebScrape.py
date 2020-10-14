#import matplotlib.pyplot as plt
#import numpy as np

import re
import requests
from bs4 import BeautifulSoup
    
tacoURLs = ("https://www.walmart.com/ip/Romaine-Lettuce-each/44391114",
        "https://www.walmart.com/ip/Great-Value-Finely-Shredded-Taco-Blend-Cheese-8-oz/10452480",
        "https://www.walmart.com/ip/All-Natural-93-Lean-7-Fat-Lean-Ground-Beef-Tray-1-lb/824841960",
        "https://www.walmart.com/ip/RO-TEL-Original-Diced-Tomatoes-and-Green-Chilies-10-Ounce/10308581",
        "https://www.walmart.com/ip/Old-El-Paso-Crunchy-Shells-Gluten-Free-18-Ct-6-89-oz-Box/10412658",
        "https://www.walmart.com/ip/Great-Value-Original-Sour-Cream-48-oz/47386251")
    
spaghettiURLs = ("https://www.walmart.com/ip/Barilla-Classic-Blue-Box-Pasta-Thick-Spaghetti-16-oz/10309191",
        "https://www.walmart.com/ip/Prego-Pasta-Sauce-Traditional-Italian-Tomato-Sauce-67-Ounce-Jar/15529694",
        "https://www.walmart.com/ip/All-Natural-93-Lean-7-Fat-Lean-Ground-Beef-Tray-1-lb/824841960",
        "https://www.walmart.com/ip/Kraft-Grated-Cheese-Parmesan-Cheese-8-oz-Jar/15716473")
    
burgerURLs = ("https://www.walmart.com/ip/Wonder-Jumbo-Seeded-Hamburger-Buns-8-ct-Bag/142899204",
        "https://www.walmart.com/ip/All-Natural-93-Lean-7-Fat-Lean-Ground-Beef-Tray-1-lb/824841960",
        "https://www.walmart.com/ip/Hellmann-s-Real-Mayonnaise-Real-Mayo-48-oz/12166718",
        "https://www.walmart.com/ip/Romaine-Lettuce-each/44391114",
        "https://www.walmart.com/ip/Sweet-Onions-each/44390992",
        "https://www.walmart.com/ip/Vlasic-Big-Crunch-Ovals-Hamburger-Dill-Chips-46-fl-oz/10308929",
        "https://www.walmart.com/ip/Ore-Ida-Golden-French-Fries-32-oz-Bag/10794811",
        "https://www.walmart.com/ip/Heinz-Tomato-Ketchup-38-oz-Bottle/22217916")
    
tunaURLs = ("https://www.walmart.com/ip/Sara-Lee-Honey-Wheat-Bread-22-slices-20-oz/10533916",
        "https://www.walmart.com/ip/Hellmann-s-Real-Mayonnaise-Real-Mayo-48-oz/12166718",
        "https://www.walmart.com/ip/StarKist-Solid-White-Albacore-Tuna-in-Vegetable-Oil-5-oz-Can/13398000",
        "https://www.walmart.com/ip/Vlasic-Big-Crunch-Ovals-Hamburger-Dill-Chips-46-fl-oz/10308929")
    
pancakesURLs = ("https://www.walmart.com/ip/Aunt-Jemima-Buttermilk-Complete-Pancake-Waffle-Mix-80-oz-Box/194717068",
        "https://www.walmart.com/ip/Mrs-Butterworths-Original-Syrup-36-fl-oz-Bottle/10449766",
        "https://www.walmart.com/ip/Great-Value-Large-White-Eggs-12-Count/145051970")
    
omeletteURLs = ("https://www.walmart.com/ip/RO-TEL-Original-Diced-Tomatoes-and-Green-Chilies-10-Ounce/10308581",
        "https://www.walmart.com/ip/Sweet-Onions-each/44390992",
        "https://www.walmart.com/ip/Great-Value-Large-White-Eggs-12-Count/145051970",
        "https://www.walmart.com/ip/Fresh-Whole-Baby-Bella-Mushrooms-16-oz/22210681",
        "https://www.walmart.com/ip/Great-Value-Finely-Shredded-Taco-Blend-Cheese-8-oz/10452480")
    
    
    
def getPrices(recipe):
        
        
    if recipe == "taco":
        recipeURLS = tacoURLs
    elif recipe == "spaghetti":
        recipeURLS = spaghettiURLs
    elif recipe == "burger":
        recipeURLS = burgerURLs
    elif recipe == "tuna":
        recipeURLS = tunaURLs
    elif recipe == "pancake":
        recipeURLS = pancakesURLs
    elif recipe == "omelette":
        recipeURLS = omeletteURLs
            
    set_of_item_prices = set()
            
    for url in recipeURLS:
        webpage = requests.get(url,headers={"User-Agent":"Defined"})
        bsoup = BeautifulSoup(webpage.content, "html.parser")
        product_name = bsoup.find(class_ = "prod-ProductTitle prod-productTitle-buyBox font-bold").get_text()
        product_price = bsoup.find(class_ = "price-group").get_text()
            
            
        tup = (product_name, product_price)
        set_of_item_prices.add(tup)
        '''
            #if re.search("Lettuce", productTitle): productTitle = "Lettuce"
            #if re.search("^Sara", productTitle): productTitle = productTitle.split(",")[0]
            
            dictPrices[productTitle] = productPrice
            '''
        
    return set_of_item_prices
    
#else: 
#    print("Warning: This module is part of the My Recipe Pal application, and is dependent on the main program to function.")
#    print("To access this module's features, please run the My Recipe Pal program.")


#taco_dict = dict(getPrices("taco"))
#tuna_dict = dict(getPrices("tuna"))
#burger_dict = dict(getPrices("burger"))
#pancake_dict = dict(getPrices("pancake"))
#omelette_dict = dict(getPrices("omelette"))
#spaghetti_dict = dict(getPrices("spaghetti")) 


#print(pancake_dict)

