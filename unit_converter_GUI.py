from tkinter import *

# Create window for GUI
window=Tk()

def unit_converter():
    print(e1_value.get())

    grams=float(e1_value.get())*1000
    t1.insert(END, grams)

    pounds=float(e1_value.get())*2.20462
    t2.insert(END, pounds)

    ozs=float(e1_value.get())*35.274
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
