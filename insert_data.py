#Module name: insert_data
#used to insert the scraped data from the web scraping modules into the database.

import sqlite3
import TargetScrape as target 
import GEWebScrape as ge
import WalMartWebScrape as walmart

conn = sqlite3.connect('stores.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS taco
           (Product_Name, Product_Price, Store)''')

c.execute('''CREATE TABLE IF NOT EXISTS tuna
           (Product_Name, Product_Price, Store)''')
           
c.execute('''CREATE TABLE IF NOT EXISTS burger
           (Product_Name, Product_Price, Store)''')   
    
c.execute('''CREATE TABLE IF NOT EXISTS pancake
           (Product_Name, Product_Price, Store)''')
   
c.execute('''CREATE TABLE IF NOT EXISTS omelette
           (Product_Name, Product_Price, Store)''')
           
c.execute('''CREATE TABLE IF NOT EXISTS spaghetti
           (Product_Name, Product_Price, Store)''')
         
# Inserts Target data into DB
'''          
for key,value in target.taco_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO taco VALUES (?, ?, ?)", (name, price, 'Target'))
    
for key,value in target.tuna_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO tuna VALUES (?, ?, ?)", (name, price, 'Target'))

for key,value in target.burger_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO burger VALUES (?, ?, ?)", (name, price, 'Target'))

for key,value in target.pancake_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO pancake VALUES (?, ?, ?)", (name, price, 'Target'))
    
for key,value in target.omelette_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO omelette VALUES (?, ?, ?)", (name, price, 'Target'))

for key,value in target.spaghetti_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO spaghetti VALUES (?, ?, ?)", (name, price, 'Target'))
'''



# Inserts GE data into DB
'''
for key,value in ge.taco_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO taco VALUES (?, ?, ?)", (name, price, 'Giant Eagle'))

for key,value in ge.tuna_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO tuna VALUES (?, ?, ?)", (name, price, 'Giant Eagle'))

for key,value in ge.burger_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO burger VALUES (?, ?, ?)", (name, price, 'Giant Eagle'))

for key,value in ge.pancake_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO pancake VALUES (?, ?, ?)", (name, price, 'Giant Eagle'))
    
for key,value in ge.omelette_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO omelette VALUES (?, ?, ?)", (name, price, 'Giant Eagle'))

for key,value in ge.spaghetti_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO spaghetti VALUES (?, ?, ?)", (name, price, 'Giant Eagle'))
'''


# Inserts Wal-Mart data into DB
'''
for key,value in walmart.taco_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO taco VALUES (?, ?, ?)", (name, price, 'Wal-Mart'))

for key,value in walmart.tuna_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO tuna VALUES (?, ?, ?)", (name, price, 'Wal-Mart'))

for key,value in walmart.burger_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO burger VALUES (?, ?, ?)", (name, price, 'Wal-Mart'))

for key,value in walmart.pancake_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO pancake VALUES (?, ?, ?)", (name, price, 'Wal-Mart'))

for key,value in walmart.omelette_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO omelette VALUES (?, ?, ?)", (name, price, 'Wal-Mart'))

for key,value in walmart.spaghetti_dict.items():
    name = key
    price = value
    c.execute("INSERT INTO spaghetti VALUES (?, ?, ?)", (name, price, 'Wal-Mart'))
'''


conn.commit()
conn.close()

