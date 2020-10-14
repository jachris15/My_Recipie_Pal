import sqlite3

conn = sqlite3.connect('stores.db')
c = conn.cursor()

'''
for row in c.execute('select * from taco'):
    print(row)

    
print('\n')

for row in c.execute('SELECT * FROM tuna'):
    print(row)

print('\n')

for row in c.execute('SELECT * from burger'):
    print(row)       

print('\n')

for row in c.execute('SELECT * from pancake'):
    print(row)
    
print('\n')

for row in c.execute('SELECT * from omelette'):
    print(row)

print('\n')
'''
for row in c.execute('SELECT * from spaghetti'):
    print(row)
