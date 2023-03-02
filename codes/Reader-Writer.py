from os import close
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD, Font 
from PIL import Image,ImageTk
from tkinter import messagebox
import threading as thread
import random
import mysql.connector
from mysql.connector.connection import MySQLConnection
from admin import admin
global Total_available_donars           
Total_available_donars = 0
lock = thread.Lock()    
class Check_Reader_Writer:
    def Recipient():
        #Recipient is searching for Blood
        lock.acquire()      
        print('Available no.of Donars :', Total_available_donars )
        lock.release()      
        print()

    def Donar():
        #Donar started Donating blood
        lock.acquire()      
        Total_available_donars  += 1              
        print('Donation completed Sucessfully!')
        lock.release()      
        print()

    if __name__ == '__main__':
        for i in range(0, 10):
            randomNumber = random.randint(0, 100)   
            if(randomNumber > 50):
                Thread1 = thread.Thread(target = Recipient)
                Thread1.start()
            else:
                Thread2 = thread.Thread(target = Donar)
                Thread2.start()

    Thread1.join()
    Thread2.join()

       

if __name__=="__main__":
    root=Tk()
    obj=Check_Reader_Writer(root)
    root.mainloop()