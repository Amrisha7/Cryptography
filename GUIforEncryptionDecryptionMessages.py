#import tkinter module
from tkinter import *
#import other necessary modules
import random
#cipher for encryption and decryption
import base64

root = Tk()
root.geometry("1200x6000")
root.title("Message Encryption & Decryption")
Tops = Frame(root,width=1600, relief=SUNKEN)
Tops.pack(side=TOP)
f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=LEFT)
lblInfo = Label(Tops, font=("Robot", 40, 'bold'),text="My Cryptography App", fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
Msg = StringVar()
key = StringVar()
mode = StringVar()
result = StringVar()
lblMsg = Label(f1, font=('arial', 16, 'bold'), text = "Message", bd=16, anchor='w') 
lblMsg.grid(row=1,column=0)
txtMsg = Entry(f1, font=('arial', 16, 'bold'), textvariable = Msg, bd=10, insertwidth=4, bg="powder blue", justify = 'right')
txtMsg.grid(row=1,column=1)

lblkey = Label(f1, font=('arial', 16, 'bold'), text = "Key", bd=16, anchor='w') 
lblkey.grid(row=2,column=0)
txtkey = Entry(f1, font=('arial', 16, 'bold'), textvariable = key, bd=10, insertwidth=4, bg="powder blue", justify = 'right')
txtkey.grid(row=2,column=1)

lblmode = Label(f1, font=('arial', 16, 'bold'), text = "Mode(e for encryption, d for decryption)", bd=16, anchor='w') 
lblmode.grid(row=3,column=0)
txtmode = Entry(f1, font=('arial', 16, 'bold'), textvariable = mode, bd=10, insertwidth=4, bg="powder blue", justify = 'right')
txtmode.grid(row=3,column=1)

lblResult = Label(f1, font=('arial', 16, 'bold'), text = "Result", bd=16, anchor='w') 
lblResult.grid(row=2,column=2)
txtResult = Entry(f1, font=('arial', 16, 'bold'), textvariable = result, bd=10, insertwidth=4, bg="powder blue", justify = 'right')
txtResult.grid(row=2,column=3)

def encode(key,msg):
    enc=[]
    for i in range(len(msg)):
        key_c = key[i%len(key)]
        enc_c = chr((ord(msg[i])+ ord(key_c))%256)
        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
def decode(key,enc):
     dec = []
     enc = base64.urlsafe_b64decode(enc).decode()
     for i in range(len(enc)):
         key_c = key[i%len(key)]
         dec_c = chr((256+ord(enc[i])-ord(key_c))%256)

         dec.append(dec_c)
     return "".join(dec)
def Results():
    msg = Msg.get()
    k= key.get()
    m = mode.get()
    if(m=='e'):
        result.set(encode(k,msg))
    else:
        result.set(decode(k,msg))
def Reset():
    Msg.set("")
    key.set("")
    mode.set("")
    Results.set("")
def Exit():
    root.destroy()

btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial',16, 'bold'), width=10, 
                  text="Show Message", bg="powder blue", 
                  command=Results).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial',16, 'bold'), width=10, 
                  text="Reset", bg="powder blue", 
                  command=Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial',16, 'bold'), width=10, 
                  text="Exit", bg="powder blue", 
                  command=Exit).grid(row=7, column=3)

root.mainloop()