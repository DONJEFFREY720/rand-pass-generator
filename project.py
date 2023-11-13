# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 18:17:08 2023

@author: Don Jeffrey
"""
from tkinter import*
import random

root=Tk()
root.title("Title") 
root.geometry("500x500")
root.configure(bg="white")

entry1 = Entry(root)

label2 = Label(root,text="YOUR PASSWORD :  ")

list1 = [[["1","2","3","4","5","6","7","8","9","0"],["!","@","#","$","%","^","&","*","(",")","=","+","-"],["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]]]

label1 = Label(root,text="STRONG PASSWORD :")

label3 = Label(root,text="STRONG PASSWORD GENERATOR")

def randnogen():
    
    label2["text"] = "YOUR PASSWORD :  "+str(entry1.get())
    
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 5)
    num3 = random.randint(0, 25)
    num4 = random.randint(0, 25)
    
    print(num1,num2,num3)

    letter1 = str(list1[0][0][num1])
    letter2 = str(list1[0][1][num2])
    letter3 = str(list1[0][2][num3])
    letter4 = str(list1[0][3][num4])

    label1["text"]="STRONG PASSWORD :  "+letter1+letter2+letter3+letter4
    
entry1.place(relx=0.5,rely=0.3,anchor=CENTER)
label2.place(relx=0.5,rely=0.4,anchor=CENTER)
btn1 = Button(root,text="GENERATE",command=randnogen)
label1.place(relx=0.5,rely=0.5,anchor=CENTER)
btn1.place(relx=0.5,rely=0.6,anchor=CENTER)
label3.place(relx=0.5,rely=0.1,anchor=CENTER)

root.mainloop()
