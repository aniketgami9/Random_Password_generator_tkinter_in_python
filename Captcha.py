import tkinter as tk
from tkinter import messagebox
from random import *
from randompassword import *

def Onclick():
    root.after(root2)

mixchars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
randomcaptcha = "".join(choice(mixchars) for x1 in range(randint(5,7)))


def check2():
    while (True):
        entry = x1.get()
        if randomcaptcha == entry:
            messagebox.showinfo("Message", "Thank You!!")
            root2.destroy()
            exit()
        else:
            messagebox.showinfo("Alert", "Try Again")
            return

root2 = tk.Tk()
root2.geometry('300x200')
root2.title("Random Password Verify")
x1 = tk.StringVar()
l3 = tk.Label(root2, text="Enter the Captcha : "+randomcaptcha)
l3.place(x=10, y=6)
e1 = tk.Entry(root2, textvariable=x1)
e1.place(x=10, y=26, width=250, height=20)
b1 = tk.Button(root2, text="continue", fg="White", bg="black", command=check2)
b1.place(x=10, y=50)
root2.mainloop()

