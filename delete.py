from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
from tkinter import messagebox

def delete():
    if os.path.exists(f'./img/{nameEntered.get().upper()}.npy'):
        os.remove(f'./img/{nameEntered.get().upper()}.npy')
        app.destroy()
    else:
        messagebox.showinfo('INFO', 'File doesnot exist')


app=Tk()
app.title("welcome")
app.geometry("400x500")
img =Image.open('delete.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(app, image=bg)
label.place(x = -2,y = -2)


img3 = Image.open('Done.jpg')
resize_img3 = img3.resize((200,60))
buttonImg2 = ImageTk.PhotoImage(resize_img3)
B2 = Button(app,command = delete,bg = 'black' ,image = buttonImg2,borderwidth=0)
B2.pack(side=BOTTOM,pady=50)

name =StringVar()
nameEntered = ttk.Entry(app, width = 50, textvariable = name)
nameEntered.pack(side=BOTTOM, ipady=8)

app.mainloop()
