"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add an entry
Update an entry
Delete
Close
"""

from tkinter import *
import backend

window=Tk()

# Create static text
l1=Label(window, text='Title')
l1.grid(row=0, column=0)# Create static text

l2=Label(window, text='Author')
l2.grid(row=0, column=2)# Create static text

l3=Label(window, text='Year')
l3.grid(row=1, column=0)# Create static text

l4=Label(window, text='ISBN')
l4.grid(row=1, column=2)

# Create entry window
e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

e2_value=StringVar()
e2=Entry(window, textvariable=e2_value)
e2.grid(row=0, column=3)

e3_value=StringVar()
e3=Entry(window, textvariable=e3_value)
e3.grid(row=1, column=1)

e4_value=StringVar()
e4=Entry(window, textvariable=e4_value)
e4.grid(row=1, column=3)

# Create list box
list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# Scroll bar
sb1=Scrollbar(window)
sb1.grid(row=2, column=2)

# Set scroll bar method along y axis
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Buttons
b1=Button(window,text="View all", width=12)
b1.grid(row=2, column=3)

b2=Button(window,text="Search Entry", width=12)
b2.grid(row=3, column=3)

b3=Button(window,text="Add Entry", width=12)
b3.grid(row=4, column=3)

b4=Button(window,text="Update Entry", width=12)
b4.grid(row=5, column=3)

b5=Button(window,text="Delete Entry", width=12)
b5.grid(row=6, column=3)

b6=Button(window,text="Close", width=12)
b6.grid(row=7, column=3)

window.mainloop()


