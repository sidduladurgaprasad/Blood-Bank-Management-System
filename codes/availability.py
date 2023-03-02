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

class availability:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1580x800+0+0")
        self.root.title("Blood Bank")

        #variables
        self.var_bg=StringVar()
        self.var_q=StringVar()

        #background 
        img=Image.open(r"D:\PROJECTS\images\avabg.jpg")
        img=img.resize((1580,850),Image.ANTIALIAS)
        self.picimg=ImageTk.PhotoImage(img)

        bg_img11=Label(self.root,image=self.picimg)
        bg_img11.place(x=0,y=0,width=1580,height=800)
        
        #label placed on background
        tlabel=Label(bg_img11,text="CHECK AVAILABILITY OF BLOOD",font=("times new roman",40,"bold"),bg="GREEN",fg="white")
        tlabel.place(x=0,y=0,width=1580,height=80)

        img11=Image.open(r"D:\PROJECTS\images\bbc.jpg")
        img11=img11.resize((1000,250),Image.ANTIALIAS)
        self.picimg11=ImageTk.PhotoImage(img11)

        img=Label(self.root,image=self.picimg11)
        img.place(x=0,y=82,width=1000,height=200)


        img12=Image.open(r"D:\PROJECTS\images\searchblood.jpg")
        img12=img12.resize((250,250),Image.ANTIALIAS)
        self.picimg12=ImageTk.PhotoImage(img12)

        img12=Label(self.root,image=self.picimg12)
        img12.place(x=1000,y=82,width=540,height=200)

        slabel=Label(bg_img11,text="SELECT BLOOD GROUP:",bg="green",fg="yellow",font=120)
        slabel.place(x=20,y=300,width=450,height=40)

        bgcombo=ttk.Combobox(bg_img11,textvariable=self.var_bg,font=(35))
        bgcombo["values"]=("Select Blood Group","A+","O+","B+","AB+","A-","O-","B-","AB-")
        bgcombo.current(0)
        bgcombo.place(x=20,y=350,width=450,height=40)

        qlabel=Label(bg_img11,text="ENTER QUANTITY IN (ML):",bg="green",fg="yellow",font=120)
        qlabel.place(x=20,y=400,width=450,height=40)

        qip=ttk.Entry(bg_img11,textvariable=self.var_q,font=(35))
        qip.place(x=125,y=150,width=150,height=20)
        qip.place(x=20,y=450,width=450,height=40)

        b1=Button(bg_img11,text="SEARCH",command=self.search,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=130,y=520,width=234,height=50)

        imglg2=Image.open(r"D:\PROJECTS\images\chart1.jpg")
        imglg2=imglg2.resize((500,500),Image.ANTIALIAS)
        self.piclg2img=ImageTk.PhotoImage(imglg2)

        f2lable=Label(self.root,image=self.piclg2img)
        f2lable.place(x=500,y=283,width=500,height=500)

        imglg3=Image.open(r"D:\PROJECTS\images\search1.jpg")
        imglg3=imglg3.resize((474,303),Image.ANTIALIAS)
        self.piclg3img=ImageTk.PhotoImage(imglg3)

        f3lable=Label(self.root,image=self.piclg3img)
        f3lable.place(x=1000,y=283,width=557,height=570)

       
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",username="root",passwd="Sarthan@123",database="blood_bank")
        mycursor=con.cursor()
        #A+
        if(self.var_bg.get()=="A+"):
            mycursor.execute("SELECT count(*) FROM donor where (bloodgroup='A+' or bloodgroup='A-' or bloodgroup='O+' or bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.var_q.get(),self.var_q.get(),))
        #O+
        elif(self.var_bg.get()=="O+"):
            mycursor.execute("SELECT count(*) FROM donor where (bloodgroup='O+' or bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.var_q.get(),self.var_q.get(),))
        #B+
        elif(self.var_bg.get()=="B+"):
            mycursor.execute("SELECT count(*) FROM donor where (bloodgroup='B+' or bloodgroup='B-' or bloodgroup='O+' or bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.var_q.get(),self.var_q.get(),))
        
        #AB+
        elif(self.var_bg.get()=="AB+"):
            mycursor.execute("SELECT count(*) FROM donor where (quantity>%s or quantity=%s) and status='pending';",(self.var_q.get(),self.var_q.get(),))
       
        #A-
        elif(self.var_bg.get()=="A-"):
            mycursor.execute("SELECT count(*) FROM donor where (bloodgroup='A-' or bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.var_q.get(),self.var_q.get(),))
        
        #O-
        elif(self.var_bg.get()=="O-"):
            mycursor.execute("SELECT count(*) FROM donor where (bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.var_q.get(),self.var_q.get(),))
        
        #B-
        elif(self.var_bg.get()=="B-"):
            mycursor.execute("SELECT count(*) FROM donor where (bloodgroup='B-' or bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.var_q.get(),self.var_q.get(),))
       
        #AB-
        elif(self.var_bg.get()=="AB-"):
            mycursor.execute("SELECT count(*) FROM donor where (bloodgroup='AB-' or bloodgroup='B-' or bloodgroup='A-' or bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.var_q.get(),self.var_q.get(),))
        
        data=mycursor.fetchall() 

        if len(data)!=0:
            self.stable.delete(*self.stable.get_children())
            for i in data:
                self.stable.insert("",END,values=i)
            con.commit()
            con.close()

    
    def search(self):
            if self.var_bg.get()=="Select Blood Group" or self.var_q.get()=="":
                messagebox.showerror("ERROR","All fields are requried",parent=self.root)
            else:
                try:
                    stable=Frame(self.root,bd=2,relief=RIDGE)
                    stable.place(x=130,y=620,width=240,height=50)


                    self.stable=ttk.Treeview(stable,column=("n"))

                    self.stable.heading("n",text="NUMBER OF DONORS AVAILABLE ARE : ")

                    self.stable["show"]="headings"

                    self.stable.column("n",width=10)

                    self.stable.pack(fill=BOTH,expand=1)
                    self.fetch_data()

                except Exception as es:
                    messagebox.showerror("ERROR",f"Due To:{str(es)}",parent=self.root)
    

        

       

if __name__=="__main__":
    root=Tk()
    obj=availability(root)
    root.mainloop()
