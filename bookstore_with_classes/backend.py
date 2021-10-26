import sqlite3

# Write backend code in the form of a class
class Database:

    # Create initial constructor/initalizer for class
    def __init__(self,db):
        conn=sqlite3.connect(db)
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        conn.commit()
        conn.close()

    # Function for adding a book record
    def insert(self,title, author, year, isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn,))
        conn.commit()
        conn.close()

    # Function for view all records button
    def view(self):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book")
        rows=cur.fetchall()
        conn.close()
        return rows

    # Function for searching records
    def search(self,title="",author="",year="",isbn=""):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book where title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows=cur.fetchall()
        conn.close()
        return rows

    # Function for deleting a record
    def delete(self,id):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()
        conn.close()

    # Function for updating a record
    def update(self,id,title,author,year,isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id,))
        conn.commit()
        conn.close()

# insert("The Earth", "John Smith", 1994, 400392029)
# delete(3)
# update(4, "The Moon", "John Smooth", "1917", 102394959)
# print(view())