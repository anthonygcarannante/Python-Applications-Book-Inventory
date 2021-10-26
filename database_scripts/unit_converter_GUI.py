from tkinter import *

# Create window for GUI
window=Tk()

def unit_converter():
    
    # Get value from input box and convert to g, lbs, oz
    grams=float(e1_value.get())*1000
    pounds=float(e1_value.get())*2.20462
    ozs=float(e1_value.get())*35.274

    # Remove existing value from text boxes and display new calculated values
    t1.delete("1.0", END)
    t1.insert(END, grams)
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ozs)

# Create static text
l1=Label(window, text='Kg')
l1.grid(row=0, column=0)

# Creating button object with location for GUI
b1=Button(window, text="Convert", command=unit_converter)
b1.grid(row=0, column=2)

# Create entry window with location
e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# Create text box with location and size
t1=Text(window, height=1, width=20)
t1.grid(row=1, column=0)
t2=Text(window, height=1, width=20)
t2.grid(row=1, column=1)
t3=Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
