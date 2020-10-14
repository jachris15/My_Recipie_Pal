import sqlite3

conn = sqlite3.connect('stores.db')
c = conn.cursor()


for row in c.execute('select * from taco'):
    print(row)
       
#for row in c.execute('SELECT * FROM tuna'):
#       print(row)
 
#for row in c.execute('SELECT * from burger'):
#    print(row)       

#for row in c.execute('SELECT * from pancake'):
#    print(row)
    
#for row in c.execute('SELECT * from omelette'):
#    print(row)

#for row in c.execute('SELECT * from pancake'):
#    print(row)