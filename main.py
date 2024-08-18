import os
import subprocess
from tkinter import *
from PIL import ImageTk, Image
import os

app = Tk()
app.title("Jarvis")
img =Image.open('WhatsApp Image 2022-01-16 at 2.35.06 PM.jpeg')
bg = ImageTk.PhotoImage(img)

app.geometry("400x550")

#Add image
label = Label(app, image=bg)
label.place(x = -2,y = -2)
# link another page
def callback():
    app.destroy()
    import first
    # filename='first.py'
    # os.system(filename)
    subprocess.Popen(["python", "first.py"])
#add button
img2 = Image.open('WhatsApp Image 2022-01-16 at 7.46.07 PM.jpeg')
resize_img2 = img2.resize((300,80))
buttonImg = ImageTk.PhotoImage(resize_img2)
B1 = Button(app,command=callback,bg = 'black' ,image = buttonImg,borderwidth=0)
B1.pack(side=BOTTOM,pady = 25)
# link another page
# Add buttons
fonts=("Times New Roman",20,"bold")
# Execute tkinter
app.mainloop()
