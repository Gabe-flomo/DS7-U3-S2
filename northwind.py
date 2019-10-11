import sqlite3 as sq
import os
os.chdir("D:\\Documents\\Atom\\Sprint challenges\\Unit 3 sprint 2")

con = sq.connect("northwind_small.sqlite3")
cur = con.cursor()

rows = cur.execute('''SELECT ProductName FROM Product
                    ORDER BY unitprice DESC LIMIT 10 ''').fetchall()
rows = str(rows)
print(f"Top 10 products are:\n {rows}")
print()

rows = cur.execute('''SELECT HireDate, BirthDate FROM Employee
                    GROUP BY HireDate 
                    ''').fetchall()
                   
#print(rows)
#print()

first = []
second = []
third = []

# calculate average age for employees hired in 2024
for i in range(3):
    hire = str(rows[i])
    bday = str(rows[i])
    hire = hire[2:6]
    bday = bday[16:20]
    age = int(hire) - int(bday)
    first.append(age)

# calculate average age for employees hired in 2025
for i in range(2):
    hire = str(rows[i])
    bday = str(rows[i])
    hire = hire[2:6]
    bday = bday[16:20]
    age = int(hire) - int(bday)
    second.append(age)

# calculate average age for employees hired in 2026
for i in range(3):
    hire = str(rows[i])
    bday = str(rows[i])
    hire = hire[2:6]
    bday = bday[16:20]
    age = int(hire) - int(bday)
    third.append(age)

print(f"The average age for employees hired in 2024 is {sum(first)//len(first)}")
print(f"The average age for employees hired in 2025 is {sum(second)//len(second)}")
print(f"The average age for employees hired in 2026 is {sum(third)//len(third)}")

rows = cur.execute('''SELECT productname, companyname
                    FROM Product JOIN Supplier ON SupplierId
                    ORDER BY unitprice DESC
                    
                    LIMIT 10
                    ''').fetchall()
print()
print(rows)
print()

rows = cur.execute('''SELECT DISTINCT max(categoryname)
                    FROM Product JOIN Category ON CategoryId                   
                    ''').fetchall()

print(f"The largst category is {str(rows[0])}")

""" 

PART 4 ANSWERS 

1) Employee and teritory have a one-to-one relationship because 
each primary key only relates to one record in the table.

2) its appropriate when wanting to have a database that multiple 
people will have access to and not just on your local machine,
or you would like to have access to it from a different location
without needing to buy  new machine. It 
wouldnt be appropriate if your storing data that that is only used locally.

3) Its a type of relational database that provides the scalability
of nosql while still maintaining atomocity, consistency, isolation, and
durability (ACID) of a traditional system.

"""