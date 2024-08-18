from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
from tkinter import filedialog as fd
import cv2

arr = []
def upload():
    filename = fd.askopenfilename()
    arr.append(filename)

def Done():
    a = nameEntered.get()
    file = './img/'+a.upper()+'.npy'
    img = cv2.imread(arr[0])
    with open(file, 'wb') as f:
        np.save(f,img)
    app.destroy()

app=Tk()
app.title("welcome")
app.geometry("400x500")
img =Image.open('Backgroundname.jpeg')
bg = ImageTk.PhotoImage(img)
#Add image
label = Label(app, image=bg)
label.place(x = -2,y = -2)

#add button
img2 = Image.open('upload.jpeg')
resize_img2 = img2.resize((300,80))
buttonImg = ImageTk.PhotoImage(resize_img2)
B1 = Button(app,bg = 'black',command=lambda: upload(),image = buttonImg,borderwidth=0)
B1.pack(side=TOP,pady = 130)


name =StringVar()
nameEntered = ttk.Entry(app, width = 50, textvariable = name)
nameEntered.pack(ipady=8)

#Done button
img3 = Image.open('Done.jpg')
resize_img3 = img3.resize((200,60))
buttonImg2 = ImageTk.PhotoImage(resize_img3)
B2 = Button(app,bg = 'black' ,image = buttonImg2,borderwidth=0,command=Done)
B2.pack(pady = 10)

app.mainloop()
