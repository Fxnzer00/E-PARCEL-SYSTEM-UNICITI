#Importing the modules
from re import L
import tkinter
import tkinter.ttk as ttk
from tkinter import *
import sqlite3
import tkinter.messagebox as tkMessageBox
from turtle import width
from tkcalendar import DateEntry
import xlsxwriter
import sqlite3
import pandas as pd
from PIL import ImageTk, Image


root = Tk()
root.title("Parcel Form CRUD")
root.geometry("1100x600+0+0")
root.config(bg="white")

# Variables required for storing the values
NAME = StringVar()
TRACKING = StringVar()
DATE = StringVar()
ID = StringVar()
FIND = StringVar()



#Function for resetting the values
def Reset():
    NAME.set("")
    TRACKING.set("")
    DATE.set("")

# For creating the database and the table
def Database():
    connectn = sqlite3.connect("parcel_data.db")
    cursor = connectn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `parcelinfo` (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT, tracking_number TEXT, status TEXT, date TEXT)")
    cursor.execute("SELECT * FROM `parcelinfo` ORDER BY `id` ASC")
    fetchinfo = cursor.fetchall()
    for data in fetchinfo:
        tree.insert('', 'end', values=(data))
    cursor.close()
    connectn.close()

#Function for exiting the system
#def Exit():
 #   O = tkMessageBox.askquestion ('Exit Application','Are you sure you want to exit?',icon = 'warning')
 #   if O > 0:
 #       root.destroy()
 #   return

#Insert query for inserting the value in database Table
def Submit():
    z='Not Receive'
    if NAME.get() == "" and TRACKING.get() == "" and DATE.get() == "":
        msgg = tkMessageBox.showerror("showerror", "Please Fill this Form")
    else:
        tree.delete(*tree.get_children())
    connectn = sqlite3.connect("parcel_data.db")
    cursor = connectn.cursor()

    cursor.execute("INSERT INTO `parcelinfo` (name, tracking_number, status, date ) VALUES(?, ?, ?, ?)", (str(NAME.get()), str(TRACKING.get()), str(z), str(DATE.get())))

    connectn.commit()
    cursor.execute("SELECT * FROM `parcelinfo` ORDER BY `name` ASC")
    fetchinfo = cursor.fetchall()

    for data in fetchinfo:
        tree.insert('', 'end', values=(data))
    cursor.close()
    connectn.close()
    NAME.set("")
    TRACKING.set("")
    DATE.set("")
  


#Update Query for updating the table in the database
def Update():
    if NAME.get() == "" and TRACKING.get() == "" and DATE.get() == "":
        msgg = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
    connectn = sqlite3.connect("parcel_data.db")
    cursor = connectn.cursor()
    cursor.execute("UPDATE `parcelinfo` SET `name` = ?, `tracking_number` = ?, `date` =? WHERE `id` = ?",
    (str(NAME.get()), str(TRACKING.get()), str(DATE.get()), int(id)))
    connectn.commit()
    cursor.execute("SELECT * FROM `parcelinfo` ORDER BY `name` ASC")
    fetchinfo = cursor.fetchall()
    for data in fetchinfo:
        tree.insert('', 'end', values=(data))

    cursor.close()
    connectn.close()

    NAME.set("")
    TRACKING.set("")
    DATE.set("")


#Module for the update contact form window
def UpdateForm(event):
    global id, UpdateWindow
    curItem = tree.focus()
    contents = (tree.item(curItem))
    item = contents['values']
    id = item[0]
    NAME.set("")
    TRACKING.set("")
    DATE.set("")

    NAME.set(item[1])
    TRACKING.set(item[2])
    DATE.set(item[4])

    


    UpdateWindow = Toplevel()
    UpdateWindow.title("User Parcel Information")
    UpdateWindow.geometry("500x520+0+0")
    UpdateWindow.resizable(0, 0)
    if 'Opennewwindow' in globals():
        Opennewwindow.destroy()

    # FRAMES
    #module is for the frame, labels, text entry, and button for update contact form window
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)

# LABELS
    label_title = Label(FormTitle, text="Edit the Parcel Information", font=('Arial', 17), bg="#189de4", width=400)
    label_title.pack(fill=X)
    label_Name = Label(ContactForm, text="Name", font=('Calibri', 14), bd=5)
    label_Name.grid(row=0, sticky=W)

    label_Tracking = Label(ContactForm, text="Tracking", font=('Calibri', 14), bd=5)
    label_Tracking.grid(row=1, sticky=W)

    label_Date = Label(ContactForm, text="Date", font=('Calibri', 14), bd=5)
    label_Date.grid(row=2, sticky=W)



# TEXT ENTRY
    entName = Entry(ContactForm, textvariable=NAME, font=('Calibri', 14, 'bold'),bd=2, width=20, justify='left')
    entName.grid(row=0, column=1)

    entTracking = Entry(ContactForm, textvariable=TRACKING, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
    entTracking.grid(row=1, column=1)

    entDate = DateEntry(ContactForm, textvariable=DATE, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
    entDate.grid(row=2, column=1)


#  Buttons
    ButtonUpdatContact = Button(ContactForm, text='Edit', bd=2, font=('Calibri', 14, 'bold'), fg="black",
    bg="#189de4", command=Update)
    ButtonUpdatContact.grid(row=8, columnspan=2, pady=10)


#Delete query for deleting the value
def Delete():
    if not tree.selection():
        msgg = tkMessageBox.showwarning('', 'Please Select the data!', icon="warning")
    else:
        msgg = tkMessageBox.askquestion('', 'Are You Sure You Want To Delete', icon="warning")
    if msgg == 'yes':
        curItem = tree.focus()
        contents = (tree.item(curItem))
        item = contents['values']
        tree.delete(curItem)
    connectn = sqlite3.connect("parcel_data.db")
    cursor = connectn.cursor()
    cursor.execute("DELETE FROM `parcelinfo` WHERE `id` = %d" % item[0])
    connectn.commit()
    cursor.close()
    connectn.close()

#For creating the frame, labels, text entry, and button for add new contact form window
def addParcel():
    global Opennewwindow
    NAME.set("")
    TRACKING.set("")
    DATE.set("")

    Opennewwindow = Toplevel()
    Opennewwindow.title("Parcel Details")
    Opennewwindow.resizable(0, 0)
    Opennewwindow.geometry("500x500+0+0")
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

#############Frames####################
    FormTitle = Frame(Opennewwindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(Opennewwindow)
    ContactForm.pack(side=TOP, pady=10)
    #RadioGroup = Frame(ContactForm)
    #not_rec = Radiobutton(RadioGroup, text="Not Receive", variable=STATUS, value="Not Receive", font=('Calibri', 14)).pack(side=LEFT)
    # ===================LABELS==============================
    label_title = Label(FormTitle, text="Adding New Parcel", bd=12,  fg="black", bg="#189de4",
    font=("Calibri", 15, "bold"), pady=2)
    label_title.pack(fill=X)
    label_Name = Label(ContactForm, text="Name", font=('Calibri', 14), bd=5)
    label_Name.grid(row=0, sticky=W)

    label_Tracking = Label(ContactForm, text="Tracking", font=('Calibri', 14), bd=5)
    label_Tracking.grid(row=1, sticky=W)

    label_Date = Label(ContactForm, text="Date", font=('Calibri', 14), bd=5)
    label_Date.grid(row=2, sticky=W)

    #label_Status = Label(ContactForm, text="Status", font=('Calibri', 14), bd=5)
    #label_Status.grid(row=3, sticky=W)




# ===================ENTRY===============================
    entName = Entry(ContactForm, textvariable=NAME, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    entName.grid(row=0, column=1)

    entTracking = Entry(ContactForm, textvariable=TRACKING, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    entTracking.grid(row=1, column=1)

    entDate = DateEntry(ContactForm, textvariable=DATE, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    entDate.grid(row=2, column=1)

   # RadioGroup.grid(row=3, column=1)



# ==================BUTTONS==============================
    ButtonAddContact = Button(ContactForm, text='Please Save', bd=5, font=('Calibri', 12, 'bold'), fg="black",
    bg="#189de4", command=Submit)
    ButtonAddContact.grid(row=7, columnspan=2, pady=10)

def downloadxcel():
    
    conn = sqlite3.connect('parcel_data.db')
    with pd.ExcelWriter("ParcelHariIni.xlsx", engine="xlsxwriter", options = {'strings_to_numbers': True, 'strings_to_formulas': False}) as writer:
        try:
            b = DATE.get()
            #df = pd.read_sql("Select * from parcelinfo WHERE date= %s" % b, conn)
            df = pd.read_sql("Select * from parcelinfo WHERE date= '8/1/22'", conn)
            df.to_excel(writer, sheet_name = "Sheet1", header = True, index = False)
           # msgg = tkMessageBox.showinfo('', 'Please Select the data!', icon="warning")
            tkMessageBox.showinfo("showinfo", "Generate Successfully")
        except:
            print("There is an error")
#script = ("SELECT * FROM parcelinfo WHERE date= %s" % b)
 #df = pd.read_sql(script, conn)

def generate():

    global Opennewwindow

    Opennewwindow = Toplevel()
    Opennewwindow.title("Generate to Excel")
    Opennewwindow.resizable(0, 0)
    Opennewwindow.geometry("500x500+0+0")
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

#############Frames####################
    FormTitle = Frame(Opennewwindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(Opennewwindow)
    ContactForm.pack(side=TOP, pady=10)

    # ===================LABELS==============================
    label_title = Label(FormTitle, text="Generate To Excel", bd=12,  fg="black", bg="#189de4",
    font=("Calibri", 15, "bold"), pady=2)
    label_title.pack(fill=X)


    label_Status = Label(ContactForm, text="Date", font=('Calibri', 14), bd=5)
    label_Status.grid(row=0, sticky=W)

# ===================ENTRY===============================

    entDate = DateEntry(ContactForm, textvariable=DATE, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    entDate.grid(row=0, column=1)


# ==================BUTTONS==============================
    ButtonAddContact = Button(ContactForm, text='Download', bd=5, font=('Calibri', 12, 'bold'), fg="black",
    bg="#189de4", command=downloadxcel)
    ButtonAddContact.grid(row=7, columnspan=2, pady=10)

def processStatus():
    if ID.get() == "":
        msgg = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        a = ID.get()
        connectn = sqlite3.connect("parcel_data.db")
        msgg = tkMessageBox.askquestion('', 'Are You Sure You Want to Change Status', icon="warning")
    if msgg == 'yes':
        cursor = connectn.cursor()
        cursor.execute("UPDATE parcelinfo SET status ='Receive' WHERE id =%s" % a)
        connectn.commit()
        cursor.close()
        connectn.close()
        msgg = tkMessageBox.showinfo("showinfo", "Succesfully Change")

#("UPDATE parcelinfo SET status ='Receive' WHERE id =%s" % a)

def statusReceive():

    global Opennewwindow

    Opennewwindow = Toplevel()
    Opennewwindow.title("Change to Receive")
    Opennewwindow.resizable(0, 0)
    Opennewwindow.geometry("500x500+0+0")
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

#############Frames####################
    FormTitle = Frame(Opennewwindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(Opennewwindow)
    ContactForm.pack(side=TOP, pady=10)

    # ===================LABELS==============================
    label_title = Label(FormTitle, text="Receive Status Change", bd=12,  fg="black", bg="#189de4",
    font=("Calibri", 15, "bold"), pady=2)
    label_title.pack(fill=X)


    label_Status = Label(ContactForm, text="ID", font=('Calibri', 14), bd=5)
    label_Status.grid(row=0, sticky=W)

# ===================ENTRY===============================

    entID = Entry(ContactForm, textvariable=ID, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    entID.grid(row=0, column=1)


# ==================BUTTONS==============================
    ButtonAddContact = Button(ContactForm, text='Change', bd=5, font=('Calibri', 12, 'bold'), fg="black",
    bg="#189de4", command=processStatus)
    ButtonAddContact.grid(row=7, columnspan=2, pady=10)


def Refresh():
    tree.delete(*tree.get_children())
    connectn = sqlite3.connect("parcel_data.db")
    cursor = connectn.cursor()
    cursor.execute("SELECT * FROM `parcelinfo` ORDER BY `id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))       
    cursor.close()
    connectn.close()

def funFind():
    if FIND.get() == "":
        msgg = tkMessageBox.showwarning('', 'Please Fill', icon="warning")
    else:
        c = FIND.get()
    tree.delete(*tree.get_children())
    connectn = sqlite3.connect("parcel_data.db")
    cursor = connectn.cursor()
    cursor.execute("SELECT * FROM parcelinfo WHERE id =%s" % c)
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))       
    cursor.close()
    connectn.close()

def click(*args):
    entFind.delete(0, 'end')
  
# call function when we leave entry box

#module for whole frame window, labels and button of contact management system
# ============================FRAMES======================================
Top = Frame(root, width=600, bd=1)
Top.pack(side=TOP)
M = Frame(root, width=650, bg="white")
M.pack(side=BOTTOM)
F = Frame(width=7, height=8, bd=10, bg="white")
F.pack(side=BOTTOM)
MR = Frame(M, width=100)
MR.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)


# LABELS
label_title = Label(Top, text="e-Parcel System Uniciti", bd=7, fg="Black", bg="#189de4",
font=("Helvetica", 25, "bold"), pady=10)
label_title.pack(fill=X)

#SEARCH BOX

entFind = Entry(Top, textvariable=FIND, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
entFind.insert(0, 'Enter ID')
entFind.pack()

entFind.bind("<Button-1>", click)

Find_Button = Button(Top, text='Find', font=('Calibri',17, 'bold'), fg="black",bg="#189de4", justify= 'right', command=funFind)
Find_Button.pack()

#entID.grid(row=0, column=1)

# BUTTONS
Add_Button = Button(F, text='Add New Parcel', font=('Calibri',17, 'bold'), fg="black",
bg="#189de4", command=addParcel).grid(row=0, column=0, ipadx=20)

Delete_Button = Button(F, text='Delete The Parcel', font=('Calibri', 17, 'bold'), command=Delete, fg="black", bg="#189de4").grid(row=0, column=1, ipadx=20)

Status_Button = Button(F, text='Status Receive', font=('Calibri', 17, 'bold'), command=statusReceive, fg="black", bg="#189de4").grid(row=0, column=2, ipadx=20)

Generate_Button = Button(F, text='Generate to Excel', font=('Calibri', 17, 'bold'), command=generate, fg="black", bg="#189de4").grid(row=0, column=3, ipadx=20)

Refresh_Button = Button(F, text='Refresh', font=('Calibri', 17, 'bold'), command=Refresh, fg="black", bg="#189de4").grid(row=0, column=4, ipadx=20)

#creating a tables in contact management system
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("", "Name", "Tracking Number", "Status", "Date"),
height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('', text="", anchor=W)
tree.heading('Name', text="Name" ,anchor=W)
tree.heading('Tracking Number', text="Tracking Number", anchor=W)
tree.heading('Status', text="Status", anchor=W)
tree.heading('Date', text="Date", anchor=W)


tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)

tree.pack()
tree.bind('<Double-Button-1>', UpdateForm)

# ============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
root.mainloop()
