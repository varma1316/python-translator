from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Enter the data in our DataBase")
root.geometry("400x400")
root.configure(bg="lightblue")  

def submit():
    con = sqlite3.connect('database.db')
    c = con.cursor()
    c.execute("INSERT INTO harshith VALUES (:f_name, :l_name, :address, :city, :state, :pincode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'pincode': pincode.get()
              })
    con.commit()
    con.close()
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    pincode.delete(0, END)

def views():
    con = sqlite3.connect('database.db')
    c = con.cursor()
    c.execute("SELECT * FROM harshith")
    re = c.fetchall()
    printre = ''
    for i in re:
        printre += str(i[0]) + " " + str(i[1]) + '\n'
    q_label = Label(root, text=printre, bg="lightblue")  
    q_label.grid(row=8, column=0, columnspan=2)

con = sqlite3.connect('database.db')
c = con.cursor()

# only once this comment need to execute
# c.execute("""CREATE TABLE harshith(first_name text,
#           last_name text,
#           address text,
#           city text,
#           state text,
#           pincode integer)
# """)

flabel = Label(root, text="First name", bg="lightblue")  
flabel.grid(row=0, column=0)
llabel = Label(root, text="Last name", bg="lightblue")  
llabel.grid(row=1, column=0)
addresslabel = Label(root, text="Address", bg="lightblue") 
addresslabel.grid(row=2, column=0)
citylabel = Label(root, text="City", bg="lightblue")  

citylabel.grid(row=3, column=0)
statelabel = Label(root, text="State", bg="lightblue")  
statelabel.grid(row=4, column=0)
pincodelabel = Label(root, text="Pincode", bg="lightblue")  

pincodelabel.grid(row=5, column=0)

submit_bts = Button(root, text="Submit data...", command=submit, bg="green", fg="white")  
submit_bts.grid(row=6, column=0, columnspan=2, pady=12, padx=12, ipadx=110)
q_bts = Button(root, text="Show Data", command=views, bg="blue", fg="white")  
q_bts.grid(row=7, column=0, columnspan=2, pady=12, padx=12, ipadx=110)

f_name = Entry(root, width=40)
f_name.grid(row=0, column=1, padx=25)
l_name = Entry(root, width=40)
l_name.grid(row=1, column=1, padx=25)
address = Entry(root, width=40)
address.grid(row=2, column=1, padx=25)
city = Entry(root, width=40)
city.grid(row=3, column=1, padx=25)
state = Entry(root, width=40)
state.grid(row=4, column=1, padx=25)
pincode = Entry(root, width=40)
pincode.grid(row=5, column=1, padx=25)

con.commit()
con.close()

root.mainloop()
