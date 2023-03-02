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

class donor:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1580x800+0+0")
        self.root.title("Blood Bank")

        #variables
        self.var_n=StringVar()
        self.var_a=StringVar()
        self.var_id=StringVar()
        self.var_bg=StringVar()
        self.var_p=StringVar()
        self.var_q=StringVar()

        #background 
        img=Image.open(r"D:\PROJECTS\images\bg2.jpg")
        img=img.resize((1580,800),Image.ANTIALIAS)
        self.picimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.picimg)
        bg_img.place(x=0,y=0,width=1530,height=1000)
        
        #label placed on background
        tlabel=Label(bg_img,text="DONOR DETAILS",font=("times new roman",40,"bold"),bg="GREEN",fg="white")
        tlabel.place(x=0,y=0,width=1580,height=80)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=80,y=150,width=1050,height=580)

        #left label frame
        lframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="DONOR DETAILS",font=50)
        lframe.place(x=5,y=10,width=485,height=560)
        img=Image.open(r"D:\PROJECTS\images\donor2.png")
        img=img.resize((470,230),Image.ANTIALIAS)
        self.pic1img=ImageTk.PhotoImage(img)

        flable=Label(lframe,image=self.pic1img)
        flable.place(x=5,y=15,width=470,height=200)

        #donor details
        nframe=LabelFrame(lframe,bd=2,relief=RIDGE,text="ENTER DETAILS",font=(30),pady=20)
        nframe.place(x=10,y=240,width=455,height=280)

        #donor name
        donorlabel=Label(nframe,text="DONOR NAME:")
        donorlabel.place(x=4,y=0,width=133,height=20)
        
        donorip=ttk.Entry(nframe,textvariable=self.var_n,width=20)
        donorip.place(x=125,y=1,width=150,height=20)

        #age
        agelabel=Label(nframe,text="AGE:")
        agelabel.place(x=0,y=30,width=83,height=20)
        
        ageip=ttk.Entry(nframe,textvariable=self.var_a,width=20)
        ageip.place(x=125,y=30,width=150,height=20)

        #donor id
        stunolabel=Label(nframe,text="DONOR ID:")
        stunolabel.place(x=0,y=60,width=118,height=20)


        rnoip=ttk.Entry(nframe,textvariable=self.var_id,width=20)
        rnoip.place(x=125,y=60,width=150,height=20)
  
        #blood group
        bglabel=ttk.Label(nframe,text="BLOOD GROUP:")
        bglabel.place(x=27,y=90,width=150,height=20)


        bgcombo=ttk.Combobox(nframe,textvariable=self.var_bg,width=20)
        bgcombo["values"]=("Select Blood Group","A+","O+","B+","AB+","A-","O-","B-","AB-")
        bgcombo.current(0)
        bgcombo.place(x=125,y=90,width=150,height=20)

        #phone no
        pnolabel=Label(nframe,text="PHONE NO:")
        pnolabel.place(x=0,y=120,width=123,height=20)
        
        donorpnoip=ttk.Entry(nframe,textvariable=self.var_p,width=20)
        donorpnoip.place(x=125,y=120,width=150,height=20)

        #quantity
        quantitylabel=Label(nframe,text="QUANTITY(ml):")
        quantitylabel.place(x=1,y=150,width=135,height=20)
        
        quantityip=ttk.Entry(nframe,textvariable=self.var_q,width=20)
        quantityip.place(x=125,y=150,width=150,height=20)


        #btn frame
        btnframe=Frame(nframe,bd=2,relief=RIDGE)
        btnframe.place(x=50,y=200,width=352,height=30)

        savebtn=Button(btnframe,command=self.add_data,text="Save",width=11,bg="blue",fg="white")
        savebtn.grid(row=0,column=0)
        updatebtn=Button(btnframe,command=self.update_data,text="Update",width=11,bg="blue",fg="white")
        updatebtn.grid(row=0,column=1)
        deletebtn=Button(btnframe,command=self.delete_data,text="Delete",width=11,bg="blue",fg="white")
        deletebtn.grid(row=0,column=2)
        resetbtn=Button(btnframe,text="Reset",command=self.reset_data,width=11,bg="blue",fg="white")
        resetbtn.grid(row=0,column=3)

        #img
        img1=Image.open(r"D:\PROJECTS\images\profile.png")
        img1=img1.resize((125,125),Image.ANTIALIAS)
        self.picimg1=ImageTk.PhotoImage(img1)

        bg_img1=Label(self.root,image=self.picimg1)
        bg_img1.place(x=400,y=475,width=125,height=125)

        #right label frame
        rframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="DISPLAY DETAILS",font=(30))
        rframe.place(x=500,y=10,width=535,height=560)

        img2=Image.open(r"D:\PROJECTS\images\details.jpg")
        img2=img2.resize((520,170),Image.ANTIALIAS)
        self.pic2img=ImageTk.PhotoImage(img2)

        f1lable=Label(rframe,image=self.pic2img)
        f1lable.place(x=5,y=10,width=520,height=150)
        

        #student table
        stable=Frame(rframe,bd=2,relief=RIDGE)
        stable.place(x=7,y=170,width=515,height=365)

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
        self.stable.bind("<ButtonRelease>",self.getcursor)
        self.fetch_data()

    #functions
    def add_data(self):
        if (self.var_n.get()=="" or self.var_a.get()=="" or self.var_id.get()=="" or self.var_bg.get()=="Select Blood Group" or self.var_p.get()=="" or self.var_q.get()==""):
            messagebox.showerror("ERROR","All Fields are required",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",passwd="Sarthan@123",database="blood_bank")
                mycursor=con.cursor()
                mycursor.execute("insert into donor values(%s,%s,%s,%s,%s,%s,'pending')",(
                                                                                    self.var_n.get(),
                                                                                    self.var_a.get(),
                                                                                    self.var_id.get(),
                                                                                    self.var_bg.get(),
                                                                                    self.var_p.get(),
                                                                                    self.var_q.get(), 
                                                                                ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox,messagebox.showinfo("SUCCESS","Donor Details has been added Successfully",parent=self.root)                                                                                                                       
            except Exception as es:
                messagebox.showerror("ERROR",f"Due To :{str(es)}",parent=self.root)                                                                    
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",username="root",passwd="Sarthan@123",database="blood_bank")
        mycursor=con.cursor()
        mycursor.execute("select * from donor ")
        data=mycursor.fetchall()

        if len(data)!=0:
            self.stable.delete(*self.stable.get_children())
            for i in data:
                self.stable.insert("",END,values=i)
            con.commit()
            con.close()

    def getcursor(self,event=""):
        cursorfocus=self.stable.focus()
        content=self.stable.item(cursorfocus)
        data=content["values"]

        self.var_n.set(data[0]),
        self.var_a.set(data[1]),
        self.var_id.set(data[2]),
        self.var_bg.set(data[3]),
        self.var_p.set(data[4]),
        self.var_q.set(data[5])

    def update_data(self):
        if (self.var_n.get()=="" or self.var_id.get()=="" or self.var_a.get()=="" or self.var_bg.get()=="Select Blood Group" or self.var_p.get()=="" or self.var_q.get()==""):
            messagebox.showerror("ERROR","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("update","Do you want to update this donor details",parent=self.root)
                if Update>0:
                    con=mysql.connector.connect(host="localhost",username="root",passwd="Sarthan@123",database="blood_bank")
                    mycursor=con.cursor()
                    mycursor.execute("update donor set donorname=%s,age=%s,bloodgroup=%s,phoneno=%s,quantity=%s,status='pending' where donorid=%s",(
                                                                                                                                         self.var_n.get(),
                                                                                                                                         self.var_a.get(),
                                                                                                                                         self.var_bg.get(),
                                                                                                                                         self.var_p.get(),
                                                                                                                                         self.var_q.get(),
                                                                                                                                         self.var_id.get()           
                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("SUCCESS","Donor details updated successfully",parent=self.root)
                con.commit()
                self.fetch_data()
                con.close()
            except Exception as es:
                messagebox.showerror("ERROR",f"Due To:{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("ERROR","DonorID must be requried",parent=self.root)
        else:
            try:
                de=messagebox.askyesno("DELETE PAGE","Do you want to delete this donor details",parent=self.root)
                if de>0:
                    con=mysql.connector.connect(host="localhost",username="root",passwd="Sarthan@123",database="blood_bank")
                    mycursor=con.cursor()
                    sql="delete from donor where donorid=%s"
                    val=(self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not de:
                        return
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("DELETE","Successfully deleted donor details",parent=self.root)
            except Exception as es:
                messagebox.showerror("ERROR",f"Due To:{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_n.set("")
        self.var_a.set("")
        self.var_id.set("")
        self.var_bg.set("Select Blood Group")
        self.var_p.set("")
        self.var_q.set("")





if __name__=="__main__":
    root=Tk()
    obj=donor(root)
    root.mainloop()
