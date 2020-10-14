import sqlite3

conn = sqlite3.connect('stores.db')
c = conn.cursor()

target = ('Target',)
walmart = ('Wal-Mart',)
ge = ('Giant Eagle',)

for row in c.execute('SELECT * FROM taco WHERE Store=?', target):
    print(row)
for row in c.execute('SELECT * FROM taco WHERE Store=?', ge):
    print(row)
for row in c.execute('SELECT * FROM taco WHERE Store=?', walmart):
    print(row)
    
print('\n')

for row in c.execute('SELECT * FROM tuna WHERE Store=?', target):
    print(row)
for row in c.execute('SELECT * FROM tuna WHERE Store=?', ge):
    print(row)
for row in c.execute('SELECT * FROM tuna WHERE Store=?', walmart):
    print(row)
    
print('\n')
    
for row in c.execute('SELECT * FROM burger WHERE Store=?', target):
    print(row)
for row in c.execute('SELECT * FROM burger WHERE Store=?', ge):
    print(row)
for row in c.execute('SELECT * FROM burger WHERE Store=?', walmart):
    print(row)
    
print('\n')

for row in c.execute('SELECT * FROM pancake WHERE Store=?', target):
    print(row)
for row in c.execute('SELECT * FROM pancake WHERE Store=?', ge):
    print(row)
for row in c.execute('SELECT * FROM pancake WHERE Store=?', walmart):
    print(row)
    
print('\n')

for row in c.execute('SELECT * FROM omelette WHERE Store=?', target):
    print(row)
for row in c.execute('SELECT * FROM omelette WHERE Store=?', ge):
    print(row)
for row in c.execute('SELECT * FROM omelette WHERE Store=?', walmart):
    print(row)
    
print('\n')

for row in c.execute('SELECT * FROM spaghetti WHERE Store=?', target):
    print(row)
for row in c.execute('SELECT * FROM spaghetti WHERE Store=?', ge):
    print(row)
for row in c.execute('SELECT * FROM spaghetti WHERE Store=?', walmart):
    print(row)
    
print('\n')

