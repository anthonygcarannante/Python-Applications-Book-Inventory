import sqlite3

def create_table():

    # 1. Connect to Database
    conn=sqlite3.connect("lite.db")

    # 2. Create cursor object
    cur=conn.cursor()

    # 3. Write an SQL Query
    cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")

    # 4. Commit changes
    conn.commit()

    # 5. Close connection
    conn.close()

def insert(item, quantity, price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

insert('Water Glass', 8, 5.50)

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

print(view())