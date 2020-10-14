import requests
import sys
import numpy as np 
from urllib.request import urlopen
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import Edge
from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By


tacoURLs = ('https://www.target.com/p/all-natural-80-20-ground-beef-1lb-good-38-gather-8482/-/A-13287606#lnk=sametab',
            'https://www.target.com/p/roma-tomato-1lb-bag/-/A-52062240#lnk=sametab',
            'https://www.target.com/p/shredded-iceberg-lettuce-8oz-good-gather-8482/-/A-54557969?ref=tgt_adv_XS000000&AFID=google_pla_df&fndsrc=tgtao&CPNG=PLA_Grocery%2BShopping_Brand&adgroup=SC_Grocery&LID=700000001170770pgs&network=g&device=c&location=9005925&ds_rl=1246978&gclid=Cj0KCQjwqrb7BRDlARIsACwGad7qXu5ugED6WVqy9kpfBRJgmElqpb2Akh4RsHpyZlpfKVK8P3aex5QaAh97EALw_wcB&gclsrc=aw.ds',
            'https://www.target.com/p/shredded-reduced-fat-mexican-style-cheese-7oz-good-38-gather-8482/-/A-54337094#lnk=sametab',
            'https://www.target.com/p/ortega-yellow-corn-taco-shells-5-8oz-12ct/-/A-13388903#lnk=sametab',
            'https://www.target.com/p/daisy-pure-38-natural-sour-cream-24oz/-/A-13451687#lnk=sametab')


spaghettiURLs = ('https://www.target.com/p/thin-spaghetti-16oz-good-38-gather-8482/-/A-78779125#lnk=sametab',
                 'https://www.target.com/p/prego-tomato-basil-garlic-italian-sauce-24-oz/-/A-14779701#lnk=sametab',
                 'https://www.target.com/p/all-natural-80-20-ground-beef-1lb-good-38-gather-8482/-/A-13287606#lnk=sametab',
                 'https://www.target.com/p/kraft-100-grated-parmesan-cheese-8-oz/-/A-12958582#lnk=sametab')

burgerURLs = ('https://www.target.com/p/hamburger-buns-11oz-8ct-market-pantry-8482/-/A-13168046#lnk=sametab',
              'https://www.target.com/p/all-natural-80-20-ground-beef-1lb-good-38-gather-8482/-/A-13287606#lnk=sametab',
              'https://www.target.com/p/mayonnaise-30oz-market-pantry-8482/-/A-13007982#lnk=sametab',
              'https://www.target.com/p/shredded-iceberg-lettuce-8oz-good-gather-8482/-/A-54557969?ref=tgt_adv_XS000000&AFID=google_pla_df&fndsrc=tgtao&CPNG=PLA_Grocery%2BShopping_Brand&adgroup=SC_Grocery&LID=700000001170770pgs&network=g&device=c&location=9005925&ds_rl=1246978&gclid=Cj0KCQjwqrb7BRDlARIsACwGad7qXu5ugED6WVqy9kpfBRJgmElqpb2Akh4RsHpyZlpfKVK8P3aex5QaAh97EALw_wcB&gclsrc=aw.ds',
              'https://www.target.com/p/yellow-onions-3lb-bag-market-pantry-8482/-/A-14916870#lnk=sametab',
              'https://www.target.com/p/kosher-hamburger-dill-chips-24oz-market-pantry-8482/-/A-76557053#lnk=sametab',
              'https://www.target.com/p/crinkle-frozen-cut-fries-32oz-market-pantry-8482/-/A-13305003#lnk=sametab',
              'https://www.target.com/p/ketchup-20oz-market-pantry-8482/-/A-14711236#lnk=sametab')



tunaURLs = ('https://www.target.com/p/nature-39-s-own-honey-wheat-bread-20oz/-/A-13159011#lnk=sametab',
            'https://www.target.com/p/mayonnaise-30oz-market-pantry-8482/-/A-13007982#lnk=sametab',
            'https://www.target.com/p/starkist-low-sodium-albacore-white-tuna-in-water-pouch-2-6-oz/-/A-13580396#lnk=sametab',
            'https://www.target.com/p/kosher-hamburger-dill-chips-24oz-market-pantry-8482/-/A-76557053#lnk=sametab')

pancakesURLs = ('https://www.target.com/p/bisquick-original-pancake-and-baking-mix-40oz/-/A-13066864#lnk=sametab',
                'https://www.target.com/p/pancake-syrup-24-fl-oz-market-pantry-8482/-/A-13007801#lnk=sametab',
                'https://www.target.com/p/grade-a-large-eggs-12ct-good-38-gather-8482/-/A-14713534#lnk=sametab')

omeletteURLs = ('https://www.target.com/p/roma-tomato-1lb-bag/-/A-52062240#lnk=sametab',
                'https://www.target.com/p/yellow-onions-3lb-bag-market-pantry-8482/-/A-14916870#lnk=sametab',
                'https://www.target.com/p/grade-a-large-eggs-12ct-good-38-gather-8482/-/A-14713534#lnk=sametab',
                'https://www.target.com/p/sliced-white-mushrooms-8oz-good-gather-8482/-/A-54567240#lnk=sametab',
                'https://www.target.com/p/shredded-reduced-fat-mexican-style-cheese-7oz-good-38-gather-8482/-/A-54337094#lnk=sametab')



def getPrices(recipe):
    
    driver = webdriver.Chrome(ChromeDriverManager().install())


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
        
        driver.get(url)
        
        product_name = driver.find_element(By.XPATH, "//h1[@data-test = 'product-title']").text
        product_price = driver.find_element(By.XPATH, "//div[@data-test = 'product-price']").text

        
        tup = (product_name, product_price)
        set_of_item_prices.add(tup)
        
    return set_of_item_prices
        
#taco_dict = dict(getPrices("taco"))
#tuna_dict = dict(getPrices("tuna"))
#burger_dict = dict(getPrices("burger"))
#pancake_dict = dict(getPrices("pancake"))
#omelette_dict = dict(getPrices("omelette"))
#spaghetti_dict = dict(getPrices("spaghetti"))        
