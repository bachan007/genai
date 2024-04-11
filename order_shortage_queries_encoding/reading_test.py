import sqlite3
import pandas as pd

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

data = cur.execute('select * from orders limit 2')

for row in data:
    print(row)

conn.commit()
conn.close()