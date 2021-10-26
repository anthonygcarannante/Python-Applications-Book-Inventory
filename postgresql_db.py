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

    # Two ways to insert values. The first is hacker prone, the second is cleaner and more secure
    # cur.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))

    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    conn.commit()
    conn.close()

# create_table()
# insert("Banana",20,2)
# delete('Banana')
update(4,12,'Banana')
print(view())