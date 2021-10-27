from tkinter import *
from backend import Database

database=Database("books.db")


class Window(object):
    
    def __init__(self, window):
        
        self.window = window

        self.window.wm_title("BookStore")

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
        self.title_text=StringVar()
        self.e1=Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text=StringVar()
        self.e2=Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_value=StringVar()
        self.e3=Entry(window, textvariable=self.year_value)
        self.e3.grid(row=1, column=1)

        self.isbn_value=StringVar()
        self.e4=Entry(window, textvariable=self.isbn_value)
        self.e4.grid(row=1, column=3)

        # Create list box
        self.list1=Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        # Scroll bar
        sb1=Scrollbar(window)
        sb1.grid(row=2, column=2)

        # Set scroll bar method along y axis
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        # Buttons
        b1=Button(window,text="View all", width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2=Button(window,text="Search Entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3=Button(window,text="Add Entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4=Button(window,text="Update Entry", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5=Button(window,text="Delete Entry", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6=Button(window,text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)

    # Stores selected value in list as event and grabs the tuple of data linked to that index entry
    def get_selected_row(self,event):

        index=self.list1.curselection()[0]
        self.selected_tuple=self.list1.get(index)

        # Update text boxes with selected row
        self.e1.delete(0,END)
        self.e1.insert(END,self.selected_tuple[1])
        self.e2.delete(0,END)
        self.e2.insert(END,self.selected_tuple[2])
        self.e3.delete(0,END)
        self.e3.insert(END,self.selected_tuple[3])
        self.e4.delete(0,END)
        self.e4.insert(END,self.selected_tuple[4])


    # Function that iterates through each row in SQL database that is stored in a list as an output. Displays each list item in listbox.
    def view_command(self):
        # Delete everything in list initially
        self.list1.delete(0,END)
        for row in database.view():
            # Inserts new row at end of the list
            self.list1.insert(END,row)

    # Search function
    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.title_text.get(),self.author_text.get(),self.year_value.get(),self.isbn_value.get()):
            self.list1.insert(END,row)

    # Add entry function
    def add_command(self):
        database.insert(self.title_text.get(),self.author_text.get(),self.year_value.get(),self.isbn_value.get())
        self.list1.delete(0,END)
        self.list1.insert(END, (self.title_text.get(),self.author_text.get(),self.year_value.get(),self.isbn_value.get()))

    # Add delete function
    def delete_command(self):
        database.delete(self.selected_tuple[0])

    # Add delete function
    def update_command(self):
        database.update(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_value.get(),self.isbn_value.get())
        print(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_value.get(),self.isbn_value.get())


window=Tk()
Window(window)
window.mainloop()
