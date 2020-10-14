import sqlite3
import TargetScrape as target 

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

conn.commit()
conn.close()