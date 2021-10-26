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

# Stores selected value in list as event and grabs the tuple of data linked to that index entry
def get_selected_row(event):
    # Create global variable to use outside of function, specifically into the delete_command function
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)

        # Update text boxes with selected row
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except:
        pass

# Function that iterates through each row in SQL database that is stored in a list as an output. Displays each list item in listbox.
def view_command():
    # Delete everything in list initially
    list1.delete(0,END)
    for row in backend.view():
        # Inserts new row at end of the list
        list1.insert(END,row)

# Search function
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),isbn_value.get(),isbn_value.get()):
        list1.insert(END,row)

# Add entry function
def add_command():
    backend.insert(title_text.get(),author_text.get(),year_value.get(),isbn_value.get())
    list1.delete(0,END)
    list1.insert(END, (title_text.get(),author_text.get(),year_value.get(),isbn_value.get()))

# Add delete function
def delete_command():
    backend.delete(selected_tuple[0])

# Add delete function
def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_value.get(),isbn_value.get())
    print(selected_tuple[0],title_text.get(),author_text.get(),year_value.get(),isbn_value.get())

window=Tk()
window.wm_title("BookStore")

# Create static text
l1=Label(window, text='Title')
l1.grid(row=0, column=0)

l2=Label(window, text='Author')
l2.grid(row=0, column=2)

l3=Label(window, text='Year')
l3.grid(row=1, column=0)

l4=Label(window, text='ISBN')
l4.grid(row=1, column=2)

# Create entry window
title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_value=StringVar()
e3=Entry(window, textvariable=year_value)
e3.grid(row=1, column=1)

isbn_value=StringVar()
e4=Entry(window, textvariable=isbn_value)
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

list1.bind('<<ListboxSelect>>',get_selected_row)

# Stores selected entry
list1.bind('<<ListboxSelect>>', get_selected_row)

# Buttons
b1=Button(window,text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window,text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window,text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window,text="Update Entry", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window,text="Delete Entry", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
