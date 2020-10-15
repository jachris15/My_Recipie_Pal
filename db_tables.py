#Final Project

import sqlite3

conn = sqlite3.connect('stores.db')
c = conn.cursor()

ge = ('Giant Eagle',)
stores = ("Wal-Mart","Target","Giant Eagle")

def get_taco():
    
    for store in stores:
        prices = {}
        listPrices = []
        for row in c.execute('SELECT Product_Price FROM taco WHERE Store=?', (store,)):
    
            listPrices.append(float(row[0].split('$')[1]))        
        
        total = sum(listPrices)
        prices[store] = total
        #for key, value in prices.items():
        #    print(key, ":", value)
    return prices
    


def get_tuna():
    
    for store in stores:
        prices = {}
        listPrices = []
        for row in c.execute('SELECT Product_Price FROM tuna WHERE Store=?', (store,)):
    
            listPrices.append(float(row[0].split('$')[1]))        
        
        total = sum(listPrices)
        prices[store] = total
        #for key, value in prices.items():
        #    print(key, ":", '$', value)
    return prices
    

def get_burger():
    
    for store in stores:
        prices = {}
        listPrices = []
        for row in c.execute('SELECT Product_Price FROM burger WHERE Store=?', (store,)):
    
            listPrices.append(float(row[0].split('$')[1]))        
        
        total = sum(listPrices)
        prices[store] = total
        #for key, value in prices.items():
        #    print(key, ":", '$', value)
    return prices
    

def get_pancake():
    
    for store in stores:
        prices = {}
        listPrices = []
        for row in c.execute('SELECT Product_Price FROM pancake WHERE Store=?', (store,)):
    
            listPrices.append(float(row[0].split('$')[1]))        
        
        total = sum(listPrices)
        prices[store] = total
        #for key, value in prices.items():
        #   print(key, ":", '$', value)
    return prices
    

#for row in c.execute('SELECT Product_Price FROM omelette WHERE Store=?', ge):
#    print(row)

def get_omelette():
    
    for store in stores:
        prices = {}
        listPrices = []
        for row in c.execute('SELECT Product_Price FROM omelette WHERE Store=?', (store,)):
            
            listPrices.append(float(row[0].split('$')[1]))        
        
        total = sum(listPrices)
        prices[store] = total
        for key, value in prices.items():
            print(key, ":", '$', value)
    return prices


def get_spaghetti():
    
    for store in stores:
        prices = {}
        listPrices = []
        for row in c.execute('SELECT Product_Price FROM spaghetti WHERE Store=?', (store,)):
    
            listPrices.append(float(row[0].split('$')[1]))        
        
        total = sum(listPrices)
        prices[store] = total
        for key, value in prices.items():
            print(key, ":", '$', value)
    return prices
    



