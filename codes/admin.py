from os import close
from pickle import INT
import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD, Font
from tkinter.tix import INTEGER 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector.connection import MySQLConnection
import cv2
from mysqlx import SqlResult
from numpy import integer


class admin:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x800+0+0")
        self.root.title("Blood Bank")

        #variables
        self.r_var_n=StringVar()
        self.r_var_a=StringVar()
        self.r_var_id=StringVar()
        self.r_var_bg=StringVar()
        self.r_var_p=StringVar()
        self.r_var_q=StringVar()
        self.d_var_n=StringVar()
        self.d_var_a=StringVar()
        self.d_var_id=StringVar()
        self.d_var_bg=StringVar()
        self.d_var_p=StringVar()
        self.d_var_q=StringVar()
        self.d_var_new_q=StringVar()
        self.t_var_id=0
        #background 
        img=Image.open(r"D:\PROJECTS\images\recbg.jpg")
        img=img.resize((1530,850),Image.ANTIALIAS)
        self.picimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.picimg)
        bg_img.place(x=0,y=0,width=1530,height=800)
        
        #label placed on background
        tlabel=Label(bg_img,text="ADMIN PAGE",font=("times new roman",40,"bold"),bg="GREEN",fg="white")
        tlabel.place(x=0,y=0,width=1530,height=80)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=82,width=1550,height=620)

        #left label frame
        lframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="RECIPIENT DETAILS",font=50)
        lframe.place(x=5,y=10,width=450,height=560)

        #donor details
        nframe=LabelFrame(lframe,bd=2,relief=RIDGE,text="ENTER DETAILS",font=(30),pady=20)
        nframe.place(x=10,y=240,width=430,height=280)

        #donor name
        donorlabel=Label(nframe,text="RECIPIENT NAME:")
        donorlabel.place(x=4,y=0,width=145,height=20)
        
        donorip=ttk.Entry(nframe,textvariable=self.r_var_n,width=20)
        donorip.place(x=125,y=1,width=150,height=20)

        #age
        agelabel=Label(nframe,text="AGE:")
        agelabel.place(x=0,y=30,width=83,height=20)
        
        ageip=ttk.Entry(nframe,textvariable=self.r_var_a,width=20)
        ageip.place(x=125,y=30,width=150,height=20)

        #donor id
        stunolabel=Label(nframe,text="RECIPIENT ID:")
        stunolabel.place(x=0,y=60,width=130,height=20)


        rnoip=ttk.Entry(nframe,textvariable=self.r_var_id,width=20)
        rnoip.place(x=125,y=60,width=150,height=20)
  
        #blood group
        bglabel=ttk.Label(nframe,text="BLOOD GROUP:")
        bglabel.place(x=27,y=90,width=150,height=20)


        bgcombo=ttk.Combobox(nframe,textvariable=self.r_var_bg,width=20)
        bgcombo["values"]=("Select Blood Group","A+","O+","B+","AB+","A-","O-","B-","AB-")
        bgcombo.current(0)
        bgcombo.place(x=125,y=90,width=150,height=20)

        #phone no
        pnolabel=Label(nframe,text="PHONE NO:")
        pnolabel.place(x=0,y=120,width=123,height=20)
        
        donorpnoip=ttk.Entry(nframe,textvariable=self.r_var_p,width=20)
        donorpnoip.place(x=125,y=120,width=150,height=20)

        #quantity
        quantitylabel=Label(nframe,text="QUANTITY(ml):")
        quantitylabel.place(x=1,y=150,width=135,height=20)
        
        quantityip=ttk.Entry(nframe,textvariable=self.r_var_q,width=20)
        quantityip.place(x=125,y=150,width=150,height=20)

        #btn frame
        btnframe=Frame(nframe,bd=2,relief=RIDGE)
        btnframe.place(x=100,y=200,width=200,height=30)

        savebtn=Button(btnframe,command=self.search_data,text="Search",width=13,bg="blue",fg="white")
        savebtn.grid(row=0,column=0)
        resetbtn=Button(btnframe,command=self.reset_data,text="Reset",width=13,bg="blue",fg="white")
        resetbtn.grid(row=0,column=1)
        #middle label frame
        rframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="DONOR DETAILS",font=(30))
        rframe.place(x=455,y=10,width=445,height=560)

        #student table
        stable=Frame(lframe,bd=2,relief=RIDGE)
        stable.place(x=5,y=10,width=435,height=230)

        scrollx=ttk.Scrollbar(stable,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(stable,orient=VERTICAL)

        self.stable=ttk.Treeview(stable,column=("n","a","id","bg","p","q"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.stable.xview)
        scrolly.config(command=self.stable.yview)

        self.stable.heading("n",text="Recipient Name")
        self.stable.heading("a",text="Age")
        self.stable.heading("id",text="Recipient ID")
        self.stable.heading("bg",text="Bloog Group")
        self.stable.heading("p",text="Phone Number")
        self.stable.heading("q",text="Quantity(ml)")

        self.stable["show"]="headings"

        self.stable.column("n",width=100)
        self.stable.column("a",width=100)
        self.stable.column("id",width=100)
        self.stable.column("bg",width=100)
        self.stable.column("p",width=100)
        self.stable.column("q",width=100)

        self.stable.pack(fill=BOTH,expand=1)
        self.stable.bind("<ButtonRelease>",self.getcursor1)
        self.fetch_data()
        #right frame
        mframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="TRANSACTION DETAILS",font=(30))
        mframe.place(x=905,y=10,width=440,height=560)

    #functions
    def row_count():
        c, conn=mysql.connector.connect(host="localhost",username="root",passwd="durga@4723",database="blood_bank")
        rowcount=c.execute("select count(*) from transaction")
        return rowcount

    def reset_data(self):
        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=0,y=82,width=1350,height=620)

        #left label frame
        lframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="RECIPIENT DETAILS",font=50)
        lframe.place(x=5,y=10,width=450,height=560)

        #donor details
        nframe=LabelFrame(lframe,bd=2,relief=RIDGE,text="ENTER DETAILS",font=(30),pady=20)
        nframe.place(x=10,y=240,width=430,height=280)

        #donor name
        donorlabel=Label(nframe,text="RECIPIENT NAME:")
        donorlabel.place(x=4,y=0,width=145,height=20)
        
        donorip=ttk.Entry(nframe,textvariable=self.r_var_n,width=20)
        donorip.place(x=125,y=1,width=150,height=20)

        #age
        agelabel=Label(nframe,text="AGE:")
        agelabel.place(x=0,y=30,width=83,height=20)
        
        ageip=ttk.Entry(nframe,textvariable=self.r_var_a,width=20)
        ageip.place(x=125,y=30,width=150,height=20)

        #donor id
        stunolabel=Label(nframe,text="RECIPIENT ID:")
        stunolabel.place(x=0,y=60,width=130,height=20)


        rnoip=ttk.Entry(nframe,textvariable=self.r_var_id,width=20)
        rnoip.place(x=125,y=60,width=150,height=20)
  
        #blood group
        bglabel=ttk.Label(nframe,text="BLOOD GROUP:")
        bglabel.place(x=27,y=90,width=150,height=20)


        bgcombo=ttk.Combobox(nframe,textvariable=self.r_var_bg,width=20)
        bgcombo["values"]=("Select Blood Group","A+","O+","B+","AB+","A-","O-","B-","AB-")
        bgcombo.current(0)
        bgcombo.place(x=125,y=90,width=150,height=20)

        #phone no
        pnolabel=Label(nframe,text="PHONE NO:")
        pnolabel.place(x=0,y=120,width=123,height=20)
        
        donorpnoip=ttk.Entry(nframe,textvariable=self.r_var_p,width=20)
        donorpnoip.place(x=125,y=120,width=150,height=20)

        #quantity
        quantitylabel=Label(nframe,text="QUANTITY(ml):")
        quantitylabel.place(x=1,y=150,width=135,height=20)
        
        quantityip=ttk.Entry(nframe,textvariable=self.r_var_q,width=20)
        quantityip.place(x=125,y=150,width=150,height=20)

        #btn frame
        btnframe=Frame(nframe,bd=2,relief=RIDGE)
        btnframe.place(x=100,y=200,width=200,height=30)

        savebtn=Button(btnframe,command=self.search_data,text="Search",width=13,bg="blue",fg="white")
        savebtn.grid(row=0,column=0)
        resetbtn=Button(btnframe,command=self.reset_data,text="Reset",width=13,bg="blue",fg="white")
        resetbtn.grid(row=0,column=1)
        
        #middle label frame
        rframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="DONOR DETAILS",font=(30))
        rframe.place(x=455,y=10,width=445,height=560)

        #student table
        stable=Frame(lframe,bd=2,relief=RIDGE)
        stable.place(x=5,y=10,width=435,height=230)

        scrollx=ttk.Scrollbar(stable,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(stable,orient=VERTICAL)

        self.stable=ttk.Treeview(stable,column=("n","a","id","bg","p","q"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.stable.xview)
        scrolly.config(command=self.stable.yview)

        self.stable.heading("n",text="Recipient Name")
        self.stable.heading("a",text="Age")
        self.stable.heading("id",text="Recipient ID")
        self.stable.heading("bg",text="Bloog Group")
        self.stable.heading("p",text="Phone Number")
        self.stable.heading("q",text="Quantity(ml")

        self.stable["show"]="headings"

        self.stable.column("n",width=100)
        self.stable.column("a",width=100)
        self.stable.column("id",width=100)
        self.stable.column("bg",width=100)
        self.stable.column("p",width=100)
        self.stable.column("q",width=100)

        self.stable.pack(fill=BOTH,expand=1)
        self.stable.bind("<ButtonRelease>",self.getcursor1)
        self.fetch_data()

        mframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="ADMIN",font=(30))
        mframe.place(x=905,y=10,width=440,height=560)

                                                                    
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",username="root",passwd="Sarthan@123",database="blood_bank")
        mycursor=con.cursor()
        mycursor.execute("select * from recipient where status='pending'")
        data1=mycursor.fetchall()

        if len(data1)!=0:
            self.stable.delete(*self.stable.get_children())
            for i in data1:
                self.stable.insert("",END,values=i)
            con.commit()
            con.close()

    def fetch_data_d(self):
        con=mysql.connector.connect(host="localhost",username="root",passwd="Sarthan@123",database="blood_bank")
        mycursor=con.cursor()
        mycursor.execute("select * From donor where status='pending'")
        data3=mycursor.fetchall()

        if len(data3)!=0:
            self.stable.delete(*self.stable.get_children())
            for i in data3:
                self.stable.insert("",END,values=i)
            con.commit()
            con.close()

    def fetch_data2(self):
        con=mysql.connector.connect(host="localhost",username="root",passwd="Sarthan@123",database="blood_bank")
        mycursor=con.cursor()
        #A+
        if(self.r_var_bg.get()=="A+"):
            mycursor.execute("SELECT * FROM donor where (bloodgroup='A+' or bloodgroup='A-' or bloodgroup='O+' or bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.r_var_q.get(),self.r_var_q.get(),))
        #O+
        elif(self.r_var_bg.get()=="O+"):
            mycursor.execute("SELECT * FROM donor where (bloodgroup='O+' or bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.r_var_q.get(),self.r_var_q.get(),))
        #B+
        elif(self.r_var_bg.get()=="B+"):
            mycursor.execute("SELECT * FROM donor where (bloodgroup='B+' or bloodgroup='B-' or bloodgroup='O+' or bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.r_var_q.get(),self.r_var_q.get(),))
        
        #AB+
        elif(self.r_var_bg.get()=="AB+"):
            mycursor.execute("SELECT * FROM donor where (quantity>%s or quantity=%s) and status='pending';",(self.r_var_q.get(),self.r_var_q.get(),))
       
        #A-
        elif(self.r_var_bg.get()=="A-"):
            mycursor.execute("SELECT * FROM donor where (bloodgroup='A-' or bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.r_var_q.get(),self.r_var_q.get(),))
        
        #O-
        elif(self.r_var_bg.get()=="O-"):
            mycursor.execute("SELECT * FROM donor where (bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.r_var_q.get(),self.r_var_q.get(),))
        
        #B-
        elif(self.r_var_bg.get()=="B-"):
            mycursor.execute("SELECT * FROM donor where (bloodgroup='B-' or bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.r_var_q.get(),self.r_var_q.get(),))
       
        #AB-
        elif(self.r_var_bg.get()=="AB-"):
            mycursor.execute("SELECT * FROM donor where (bloodgroup='AB-' or bloodgroup='B-' or bloodgroup='A-' or bloodgroup='O-' ) and (quantity>%s or quantity=%s) and status='pending';",(self.r_var_q.get(),self.r_var_q.get(),))
        
        data=mycursor.fetchall() 

        if len(data)!=0:
            self.stable.delete(*self.stable.get_children())
            for i in data:
                self.stable.insert("",END,values=i)
            con.commit()
            con.close()


    def getcursor1(self,event=""):
        cursorfocus1=self.stable.focus()
        content1=self.stable.item(cursorfocus1)
        data1=content1["values"]

        self.r_var_n.set(data1[0]),
        self.r_var_a.set(data1[1]),
        self.r_var_id.set(data1[2]),
        self.r_var_bg.set(data1[3]),
        self.r_var_p.set(data1[4]),
        self.r_var_q.set(data1[5])

    def getcursor2(self,event=""):
        cursorfocus2=self.stable.focus()
        content2=self.stable.item(cursorfocus2)
        data2=content2["values"]

        self.d_var_n.set(data2[0]),
        self.d_var_a.set(data2[1]),
        self.d_var_id.set(data2[2]),
        self.d_var_bg.set(data2[3]),
        self.d_var_p.set(data2[4]),
        self.d_var_q.set(data2[5])

    def search_data(self):
        if (self.r_var_n.get()=="" or self.r_var_a.get()=="" or self.r_var_id.get()=="" or self.r_var_bg.get()=="Select Blood Group" or self.r_var_p.get()=="" or self.r_var_q.get()==""):
            messagebox.showerror("ERROR","All Fields are required",parent=self.root)
        else:
            try:
                
                stable=Frame(self.root,bd=2,relief=RIDGE)
                stable.place(x=465,y=122,width=435,height=232)

                scrollx=ttk.Scrollbar(stable,orient=HORIZONTAL)
                scrolly=ttk.Scrollbar(stable,orient=VERTICAL)

                self.stable=ttk.Treeview(stable,column=("n","a","id","bg","p","q"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)
                scrollx.config(command=self.stable.xview)
                scrolly.config(command=self.stable.yview)

                self.stable.heading("n",text="Donor Name")
                self.stable.heading("a",text="Age")
                self.stable.heading("id",text="Donor ID")
                self.stable.heading("bg",text="Bloog Group")
                self.stable.heading("p",text="Phone Number")
                self.stable.heading("q",text="Quantity(ml)")

                self.stable["show"]="headings"

                self.stable.column("n",width=100)
                self.stable.column("a",width=100)
                self.stable.column("id",width=100)
                self.stable.column("bg",width=100)
                self.stable.column("p",width=100)
                self.stable.column("q",width=100)

                self.stable.pack(fill=BOTH,expand=1)
                self.stable.bind("<ButtonRelease>",self.getcursor2)
                self.fetch_data2()
                

                #donor details
                nframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="ENTER DETAILS",font=(30),pady=20)
                nframe.place(x=465,y=360,width=430,height=280)

                #donor name
                donorlabel=Label(nframe,text="DONOR NAME:")
                donorlabel.place(x=4,y=0,width=133,height=20)
                
                donorip=ttk.Entry(nframe,textvariable=self.d_var_n,width=20)
                donorip.place(x=125,y=1,width=150,height=20)

                #age
                agelabel=Label(nframe,text="AGE:")
                agelabel.place(x=0,y=30,width=83,height=20)
                
                ageip=ttk.Entry(nframe,textvariable=self.d_var_a,width=20)
                ageip.place(x=125,y=30,width=150,height=20)

                #donor id
                stunolabel=Label(nframe,text="DONOR ID:")
                stunolabel.place(x=0,y=60,width=118,height=20)


                rnoip=ttk.Entry(nframe,textvariable=self.d_var_id,width=20)
                rnoip.place(x=125,y=60,width=150,height=20)
        
                #blood group
                bglabel=ttk.Label(nframe,text="BLOOD GROUP:")
                bglabel.place(x=27,y=90,width=150,height=20)


                bgcombo=ttk.Combobox(nframe,textvariable=self.d_var_bg,width=20)
                bgcombo["values"]=("Select Blood Group","A+","O+","B+","AB+","A-","O-","B-","AB-")
                bgcombo.current(0)
                bgcombo.place(x=125,y=90,width=150,height=20)

                #phone no
                pnolabel=Label(nframe,text="PHONE NO:")
                pnolabel.place(x=0,y=120,width=123,height=20)
                
                donorpnoip=ttk.Entry(nframe,textvariable=self.d_var_p,width=20)
                donorpnoip.place(x=125,y=120,width=150,height=20)

                #quantity
                quantitylabel=Label(nframe,text="QUANTITY(ml):")
                quantitylabel.place(x=1,y=150,width=135,height=20)
                
                quantityip=ttk.Entry(nframe,textvariable=self.d_var_q,width=20)
                quantityip.place(x=125,y=150,width=150,height=20)
            
                #btn frame
                btnframe2=Frame(nframe,bd=2,relief=RIDGE)
                btnframe2.place(x=100,y=200,width=200,height=30)

                b4=Button(self.root,text="Supply",command=self.supply,cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="white")
                b4.place(x=530,y=580,width=300,height=50)

                messagebox.showinfo("NOTE","Click Reset Button For Next Search",parent=self.root)                                         
            except Exception as es:
                messagebox.showerror("ERROR",f"Due To :{str(es)}",parent=self.root)
                                      
    def supply(self):
        if (self.d_var_id.get()=="" or self.r_var_id.get()==""):
            messagebox.showerror("ERROR","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",passwd="Sarthan@123",database="blood_bank")
                cursor1=conn.cursor()
                cursor1.execute("select count(*) from transaction") 
                d=cursor1.fetchone()[0]
                self.t_var_id=d+1

                conn.close()
                con=mysql.connector.connect(host="localhost",username="root",passwd="Sarthan@123",database="blood_bank")
                mycursor=con.cursor()
                mycursor.execute("insert into transaction values(%s,%s,%s)",(
                                                                                    self.t_var_id,
                                                                                    self.d_var_id.get(),
                                                                                    self.r_var_id.get(),
                                                                                ))
                con.commit()
                self.fetch_data_t()
                con.close()
                self.t_var_id=self.t_var_id+1

                stable=Frame(self.root,bd=2,relief=RIDGE)
                stable.place(x=465,y=122,width=435,height=232)

                scrollx=ttk.Scrollbar(stable,orient=HORIZONTAL)
                scrolly=ttk.Scrollbar(stable,orient=VERTICAL)

                self.stable=ttk.Treeview(stable,column=("n","a","id","bg","p","q"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)
                scrollx.config(command=self.stable.xview)
                scrolly.config(command=self.stable.yview)

                self.stable.heading("n",text="Donor Name")
                self.stable.heading("a",text="Age")
                self.stable.heading("id",text="Donor ID")
                self.stable.heading("bg",text="Bloog Group")
                self.stable.heading("p",text="Phone Number")
                self.stable.heading("q",text="Quantity(ml)")

                self.stable["show"]="headings"

                self.stable.column("n",width=100)
                self.stable.column("a",width=100)
                self.stable.column("id",width=100)
                self.stable.column("bg",width=100)
                self.stable.column("p",width=100)
                self.stable.column("q",width=100)

                self.stable.pack(fill=BOTH,expand=1)
                self.stable.bind("<ButtonRelease>",self.getcursor2)
                self.fetch_data2()

                stable=Frame(self.root,bd=2,relief=RIDGE)
                stable.place(x=925,y=122,width=410,height=230)

                scrollx=ttk.Scrollbar(stable,orient=HORIZONTAL)
                scrolly=ttk.Scrollbar(stable,orient=VERTICAL)

                self.stable=ttk.Treeview(stable,column=("n","a","id"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)
                scrollx.config(command=self.stable.xview)
                scrolly.config(command=self.stable.yview)

                self.stable.heading("n",text="Transaction ID")
                self.stable.heading("a",text="Donor ID")
                self.stable.heading("id",text="Recipient ID")


                self.stable["show"]="headings"

                self.stable.column("n",width=100)
                self.stable.column("a",width=100)
                self.stable.column("id",width=100)


                self.stable.pack(fill=BOTH,expand=1)
                self.stable.bind("<ButtonRelease>")
                self.fetch_data_t()

                con=mysql.connector.connect(host="localhost",username="root",passwd="Sarthan@123",database="blood_bank")
                mycursor=con.cursor()

                if (self.d_var_q.get()==self.r_var_q.get()):
                    try:
                        mycursor.execute("update donor,recipient set donor.status='success',recipient.status='success' where donor.donorid=%s and recipient.recipientid=%s",(
                                                                                                                                                                                self.d_var_id.get(),
                                                                                                                                                                                self.r_var_id.get()
                                                                                                                                                                                ))
                    except Exception as es:
                        messagebox.showerror("ERROR",f"Due To :{str(es)}",parent=self.root) 

                else :
                    try:
                        self.x=int(self.d_var_q.get())
                        self.y=int(self.r_var_q.get())
                        self.d_var_new_q=self.x-self.y
                        mycursor.execute("update donor,recipient set donor.quantity=%s,recipient.status='success' where donor.donorid=%s and recipient.recipientid=%s",(
                                                                                                                                                        self.d_var_new_q,
                                                                                                                                                        self.d_var_id.get(),
                                                                                                                                                        self.r_var_id.get()
                                                                                                                                                        ))
                    except Exception as es:
                        messagebox.showerror("ERROR",f"Due To :{str(es)}",parent=self.root) 
                con.commit()
                con.close()

                img13=Image.open(r"D:\PROJECTS\images\completed.jpg")
                img13=img13.resize((400,200),Image.ANTIALIAS)
                self.pic13img=ImageTk.PhotoImage(img13)

                flable=Label(self.root,image=self.pic13img)
                flable.place(x=925,y=370,width=400,height=200)

                b3=Button(self.root,text="Next Transaction",command=self.reset_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
                b3.place(x=980,y=580,width=300,height=50)

                messagebox,messagebox.showinfo("SUCCESS","Transaction has been done Successfully",parent=self.root)                                                                                                                       
            except Exception as es:
                messagebox.showerror("ERROR",f"Due To :{str(es)}",parent=self.root) 

    def fetch_data_t(self):
        con=mysql.connector.connect(host="localhost",username="root",passwd="Sarthan@123",database="blood_bank")
        mycursor4=con.cursor()
        mycursor4.execute("select * from transaction ")
        data4=mycursor4.fetchall()

        if len(data4)!=0:
            self.stable.delete(*self.stable.get_children())
            for i in data4:
                self.stable.insert("",END,values=i)
            con.commit()
            con.close()





if __name__=="__main__":
    root=Tk()
    obj=admin(root)
    root.mainloop()
