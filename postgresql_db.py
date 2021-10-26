# Database via postgresql
import psycopg2

def create_table():

    # 1. Connect to Database
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")

    # 2. Create cursor object
    cur=conn.cursor()

    # 3. Write an SQL Query
    cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")

    # 4. Commit changes
    conn.commit()

    # 5. Close connection
    conn.close()

def insert(item, quantity, price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item, quantity, price))
    conn.commit()
    conn.close()

# create_table()
insert("Apple",10,15)