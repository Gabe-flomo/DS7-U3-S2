import sqlite3 as sq

con = sq.connect('demo_data.sqlite3')
cur = con.cursor()

create_table = ''' CREATE TABLE demo
            (s TEXT,
            x INTEGER,
            y INTEGER)'''

data = [['g',3,9],
        ['v',5,7],
        ['f',8,7]]

#cur.execute(create_table)
#cur.execute('DELETE FROM demo')

"""cur.execute(''' INSERT INTO demo
            VALUES ('g', 3, 9)''')

cur.execute(''' INSERT INTO demo
            VALUES ('v', 5, 7)''')

cur.execute(''' INSERT INTO demo
            VALUES ('f', 8, 7)''')"""

con.commit()


rows = cur.execute('''SELECT * FROM demo''').fetchall()
print(f"There are {len(rows)} rows: ",rows)
print()
rows = cur.execute('SELECT x,y FROM demo where x >= 5 AND y >= 5 ').fetchall()
print(f"There are {len(rows)} where x and y >= 5:",rows)
print()
rows = cur.execute(' SELECT DISTINCT y FROM demo ').fetchall()
print(f"There are {len(rows)} distinct values: ",rows)
con.close()