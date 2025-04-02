
from msilib.schema import Font
from tkinter import *
from turtle import width
from PIL import Image, ImageTk

window = Tk()
window.title("Login e-Parcel")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width =750
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.resizable(0, 0)

#=========================================Function For Login===================================

def logIn():
    if USER.get() == "admin" and PASS.get() == "1234":
        window.destroy()
        import formcrud

    elif USER.get() == "" and PASS.get() == "":
        txt_result.config(text="Please fill in the box", fg="red", bg='white')

    else:
        txt_result.config(text="Password Incorect", fg="red", bg='white')

#================================Variables required for storing the values======================
USER=StringVar()
PASS=StringVar()

#================================Variables required for storing the values======================
f1 = Frame(window,bg="#189de4", width=450, height=500)
f1.pack(side=LEFT)
f1.pack_propagate(0)

#==============================Image Unimap Logo======================================
image = Image.open("unimap.png")

resize_image = image.resize((200, 150 ))
 
img = ImageTk.PhotoImage(resize_image)
 
label1 = Label(f1, bg= '#189de4', image=img)
label1.image = img
label1.pack(pady=10)

x = Label(f1, text="SYSTEM E-PARCEL UNICITI",bg="#189de4",justify=CENTER, font=('Helvetica 20 bold'), fg="white").pack(pady= 50)

f2 = Frame(window, bg="white", width=300, height=500)
f2.pack(side=RIGHT)
f2.pack_propagate(0)
a = Label(f2, text="ADMIN LOG IN",bg="white",justify=CENTER,font=('Helvetica 20 bold')).pack(pady= 45)

#================================User Pass Entry======================
b =Label(f2, text="User",bg="white",justify=CENTER,font=('Helvetica 15 bold')).pack(pady= 15)
ent_user = Entry(f2, width=40, bg="#bebebe", textvariable=USER).pack(pady=15)

c =Label(f2, text="Password",bg="white",justify=CENTER,font=('Helvetica 15 bold')).pack(pady= 15)
ent_pass = Entry(f2, width=40, show='*', bg="#bebebe", textvariable=PASS).pack(pady=15)
btn_login = Button(f2,text="Log In", bg="#189de4", command=logIn).pack(pady=15)


txt_result = Label(f2, justify=CENTER )
txt_result.pack()

window.mainloop()