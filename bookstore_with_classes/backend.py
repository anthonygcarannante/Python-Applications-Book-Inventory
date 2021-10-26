import sqlite3

# Write backend code in the form of a class
class Database:

    # Create initial constructor/initalizer for class
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    # Function for adding a book record
    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn,))
        self.conn.commit()

    # Function for view all records button
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    # Function for searching records
    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book where title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows

    # Function for deleting a record
    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    # Function for updating a record
    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
