from tkinter import *
import sqlite3
import pyttsx3
import tkinter.messagebox
# connection to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# empty lists to append later
number = []
patients = []

sql = "SELECT * FROM appointments"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)

# window
class Application:
    def __init__(self, master):
        self.master = master
        self.x = 0
        # heading
        self.heading = Label(master, text="Bookings", font=('arial 60 bold'), fg='green')
        self.heading.place(x=700, y=0)

        # button to change bookings
        self.change = Button(master, text="Next Booking", width=25, height=2, bg='steelblue', command=self.func)
        self.change.place(x=800, y=600)

        # empty text labels to later config
        self.n = Label(master, text="", font=('arial 200 bold'))
        self.n.place(x=800, y=100)

        self.pname = Label(master, text="", font=('arial 80 bold'))
        self.pname.place(x=650, y=400)
    # function to speak the text and update the text

    def func(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 50)
        engine.say('Booking number ' + str(number[self.x]) + str(patients[self.x]))
        engine.runAndWait()
        self.x += 1

class Application1:
    def __init__(self, master):
        self.master = master
        # heading label
        self.heading = Label(master, text="Bookings ",  fg='grey', font=('arial 40 bold'))
        self.heading.place(x=150, y=20)

        # search criteria -->name
        self.name = Label(master, text="Enter Owner's Name", font=('arial 18 bold'))
        self.name.place(x=0, y=100)

        # entry for  the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280, y=92)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=132)
    # function to search
    def search_db(self):
        self.input = self.namenet.get()
        # execute sql

        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]
        # creating the update form
        self.uname = Label(self.master, text="Owner's Name", font=('arial 18 bold'))
        self.uname.place(x=0, y=160)

        self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
        self.uage.place(x=0, y=200)

        self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
        self.ugender.place(x=0, y=240)

        self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
        self.ulocation.place(x=0, y=280)

        self.utime = Label(self.master, text="Entry Time", font=('arial 18 bold'))
        self.utime.place(x=0, y=320)

        self.uphone = Label(self.master, text="Phone Number", font=('arial 18 bold'))
        self.uphone.place(x=0, y=360)

        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=170)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=210)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=250)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=290)
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=330)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=370)
        self.ent6.insert(END, str(self.phone))

        # button to execute update
        self.update = Button(self.master, text="Update?", width=20, height=2,fg='white', bg='black', command=self.update_db)
        self.update.place(x=400, y=410)

        # button to delete
        self.delete = Button(self.master, text="Delete?", width=20, height=2,fg='white', bg='black', command=self.delete_db)
        self.delete.place(x=150, y=410)
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() #updated age
        self.var3 = self.ent3.get() #updated gender
        self.var4 = self.ent4.get() #updated location
        self.var5 = self.ent5.get() #updated phone
        self.var6 = self.ent6.get() #updated time

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
class List():
    def __init__(self):
        self.tk = tkinter
        self.listbox = self.tk.Listbox(root)
        self.listbox.pack()

    def clicked(self):
        self.listbox.insert(self.tk.END, self.content.get())

    def delete(self):
        self.listbox.delete(0, self.tk.END)

    def delete_selected(self):
        self.listbox.delete(self.tk.ANCHOR)

    def function(self):
        self.content = patients
        self.entry = self.tk.Entry(root, textvariable=self.content)
        self.entry.pack()
        self.button = self.tk.Button(root, text="Add Item", command=self.clicked)
        self.button.pack()
        self.button_delete = self.tk.Button(text="Delete", command=self.delete)
        self.button_delete.pack()
        self.button_delete_selected = self.tk.Button(text="Delete Selected", command=self.delete_selected)
        self.button_delete_selected.pack()

# creating the object
root = Tk()
a = List()
b = Application(root)
d = Application1(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()
