import tkinter as tk
from tkinter import messagebox
from random import *

mixint= "0123456789"
mixchars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
randomcaptcha = "".join(choice(mixchars) for x1 in range(randint(5,7)))
randompass = "".join(choice(mixint) for x in range(randint(4,5)))


def check():
        while (True):
            userentry = x.get()
            if randompass == userentry:
                messagebox.showinfo("Message", "Login Successfully")
                root.destroy()
                break
            else:
                messagebox.showinfo("Alert", "Try Again")
                return

root = tk.Tk()
root.geometry('300x200')
root.title("Random Password")
x = tk.StringVar()
l = tk.Label(root, text="Here is your password : " + randompass)
l.place(x=10, y=3)
e = tk.Entry(root, textvariable=x)
e.place(x=10, y=26, width=250, height=20)
b = tk.Button(root, text="Submit & verify", fg="White", bg="black", command=check)
b.place(x=10, y=50)

root.mainloop()

