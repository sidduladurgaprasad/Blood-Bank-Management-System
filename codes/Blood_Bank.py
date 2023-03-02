from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD, Font 
from PIL import Image,ImageTk
from login import login
from recipient import recipient
from donor import donor
from availability import availability

class Blood_Bank:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        
        self.root.title("Blood Bank")
        
        #background 
        img=Image.open(r"D:\PROJECTS\images\home_bg.jpg")
        img=img.resize((1530,800),Image.ANTIALIAS)
        self.picimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.picimg)
        bg_img.place(x=0,y=0,width=1530,height=800)
        
        #label placed on background
        tlabel=Label(bg_img,text="BLOOD BANK",font=("times new roman",40,"bold"),fg="RED")
        tlabel.place(x=700,y=0,width=600,height=80)

        #icon
        i3=Image.open(r"D:\PROJECTS\images\icon.jpeg")
        i3=i3.resize((75,90),Image.ANTIALIAS)
        self.picoimg=ImageTk.PhotoImage(i3)
        b=Label(image=self.picoimg,cursor="hand2")
        b.place(x=1200,y=0,width=75,height=75)

        #button-1
        img3=Image.open(r"D:\PROJECTS\images\donor1.png")
        img3=img3.resize((320,235),Image.ANTIALIAS)
        self.pic3img=ImageTk.PhotoImage(img3)

        b3=Button(bg_img,command=self.dnr,image=self.pic3img,cursor="hand2")
        b3.place(x=700,y=130,width=234,height=200)

        b3=Button(bg_img,text="Donar Details",command=self.dnr,cursor="hand2",font=("monospace",15,"bold"),bg="green",fg="white")
        b3.place(x=700,y=330,width=234,height=50)

        #button-2
        img4=Image.open(r"D:\PROJECTS\images\recipient.png")
        img4=img4.resize((320,240),Image.ANTIALIAS)
        self.pic4img=ImageTk.PhotoImage(img4)

        b4=Button(bg_img,command=self.rec,image=self.pic4img,cursor="hand2")
        b4.place(x=1100,y=130,width=234,height=200)

        b4=Button(bg_img,command=self.rec,text="Recipient Details",cursor="hand2",font=("monospace",15,"bold"),bg="blue",fg="white")
        b4.place(x=1100,y=330,width=234,height=50)
     
        #button-3
        img5=Image.open(r"D:\PROJECTS\images\chk.jpg")
        img5=img5.resize((234,240),Image.ANTIALIAS)
        self.pic5img=ImageTk.PhotoImage(img5)

        b5=Button(bg_img,command=self.ava,image=self.pic5img,cursor="hand2")
        b5.place(x=700,y=450,width=234,height=200)

        b5=Button(bg_img,command=self.ava,text="Check Availability",cursor="hand2",font=("monospace",15,"bold"),bg="orange",fg="white")
        b5.place(x=700,y=650,width=234,height=50)

        #button-4
        img6=Image.open(r"D:\PROJECTS\images\ad.jpg")
        img6=img6.resize((234,200),Image.ANTIALIAS)
        self.pic6img=ImageTk.PhotoImage(img6)

        b6=Button(bg_img,command=self.log,image=self.pic6img,cursor="hand2")
        b6.place(x=1100,y=450,width=234,height=200)

        b6=Button(bg_img,command=self.log,text="Login as Admin",cursor="hand2",font=("monospace",15,"bold"),bg="purple",fg="white")
        b6.place(x=1100,y=650,width=234,height=50)

     
    # functions
    def dnr(self):
        self.newpage=Toplevel(self.root)
        self.app=donor(self.newpage)
    
    def rec(self):
        self.newpage=Toplevel(self.root)
        self.app=recipient(self.newpage)
    
    def ava(self):
        self.newpage=Toplevel(self.root)
        self.app=availability(self.newpage)
    
    def log(self):
        self.newpage=Toplevel(self.root)
        self.app=login(self.newpage)
        




if __name__=="__main__":
    root=Tk()
    obj=Blood_Bank(root)
    root.mainloop()
