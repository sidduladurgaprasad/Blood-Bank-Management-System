from os import close
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD, Font 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector.connection import MySQLConnection
import cv2
from admin import admin

class login:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1580x800+0+0")
        self.root.title("Blood Bank")

        #variables
        self.name=StringVar()
        self.password=StringVar()

        #background 
        img=Image.open(r"D:\PROJECTS\images\login.jpg")
        img=img.resize((1580,800),Image.ANTIALIAS)
        self.picimg=ImageTk.PhotoImage(img)

        bg_imgl1=Label(self.root,image=self.picimg)
        bg_imgl1.place(x=0,y=0,width=1580,height=800)


        usernameip=ttk.Entry(bg_imgl1,textvariable=self.name,font=("times new roman",35,"bold"))
        usernameip.place(x=295,y=325,width=800,height=60)

        passwardip=ttk.Entry(bg_imgl1,textvariable=self.password,show='*',font=("times new roman",35,"bold"))
        passwardip.place(x=295,y=465,width=800,height=60)

        b1=Button(bg_imgl1,text="LOGIN",command=self.login_page,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=400,y=534,width=234,height=50)
        
        imglg1=Image.open(r"D:\PROJECTS\images\user.png")
        imglg1=imglg1.resize((97,62),Image.ANTIALIAS)
        self.picimglg1=ImageTk.PhotoImage(imglg1)

        bg_imglg1=Label(self.root,image=self.picimglg1)
        bg_imglg1.place(x=198,y=325,width=97,height=62)

        imglg2=Image.open(r"D:\PROJECTS\images\passward.jpg")
        imglg2=imglg2.resize((97,62),Image.ANTIALIAS)
        self.picimglg2=ImageTk.PhotoImage(imglg2)

        bg_imglg2=Label(self.root,image=self.picimglg2)
        bg_imglg2.place(x=198,y=465,width=97,height=62)

    def login_page(self):
        if self.name.get()=='admin' and self.password.get()=='admin@123':
            try:
                b2=Button(self.root,text="next",command=self.adm,cursor="hand2",font=("times new roman",25,"bold"),bg="green",fg="white")
                b2.place(x=650,y=534,width=234,height=50)
                messagebox.showinfo("SUCCESS","Please click on next",parent=self.root)
            except Exception as es:
                messagebox.showerror("ERROR",f"Due To :{str(es)}",parent=self.root)
        else:
            messagebox.showerror("ERROR","Please check your details",parent=self.root)
    
    def adm(self):
        self.newpage=Toplevel(self.root)
        self.app=admin(self.newpage)

       

if __name__=="__main__":
    root=Tk()
    obj=login(root)
    root.mainloop()
