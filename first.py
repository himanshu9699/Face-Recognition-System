import subprocess
from tkinter import *
from PIL import ImageTk, Image
from datetime import date
import cv2
import numpy as np
import os
import face_recognition
from tkinter import messagebox

def take():
    currentDate = date.today()
    newDate = currentDate.strftime("%d-%m-%y")
    try:
        with open(f'attendance{newDate}.csv', 'x') as f:
            f.write(f'Name,Attendance')
    except:
        messagebox.showinfo('INFO',"File Already Exist")
        return None

    path = 'img'
    images = []
    className = []
    myList = os.listdir(path)
    print(myList)
    for cls in myList:
        with open('./img/'+cls,'rb') as f:
            matrix = np.load(f)
            images.append(matrix)
            className.append(os.path.splitext(cls)[0])

    print(images)
    print(className)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def attendance(person):
        currentDate = date.today()
        newDate = currentDate.strftime("%d-%m-%y")
        with open(f'./attendance{newDate}.csv', 'r+') as f:
            data = f.readlines()
            nameList = []
            print(data)
            for i in data:  ### ['Name,Attendence']
                name = i.split(',')  ## ['Name','Ateendence']
                nameList.append(name[0])
                print(name)
            if person not in nameList:
                f.writelines(f'\n{person},P')
        # print(data)
    encodeListKnown = findEncodings(images)
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()  ## True , img--> []
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        facesCurFrame = face_recognition.face_locations(imgRGB)
        encodesCurFrame = face_recognition.face_encodings(imgRGB, facesCurFrame)  ## [127 mes]

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)
            # print(matchIndex)
            # print(matches)
            # print(len(encodeFace))

            if matches[matchIndex]:
                name = className[matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLoc
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
                attendance(name)
        cv2.imshow('WEBCAM', img)
        if cv2.waitKey(1) == 27:
            break
    #
    cap.release()
    cv2.destroyAllWindows()



### UI

app=Tk()
app.title("welcome")
app.geometry("400x500")
img =Image.open('bg.jpeg')
bg = ImageTk.PhotoImage(img)
label = Label(app, image=bg)
label.place(x = -2,y = -2)
#defining functions
def callback():
    app.destroy()
    # filename= 'add.py'
    # os.system('add.py')
    subprocess.Popen(["python", "add.py"])
    # os.access('add.py')
def callback2():
    app.destroy()
    subprocess.Popen(["python", "delete.py"])
    # filename1='delete.py'
    # os.system(filename1)
#----------------------------------
#add button1
#f1=Frame(app,bg="21.jpeg")
# f1.pack(side=BOTTOM,pady=30)
img2 = Image.open('addbutton.jpeg')
resize_img2 = img2.resize((300,80))
buttonImg = ImageTk.PhotoImage(resize_img2)
B1 = Button(app,command=callback,bg = '#1B7358' ,image = buttonImg,borderwidth=0)
B1.grid(row=0,rowspan=2,column=0,padx=50,pady=150)
#addbutton2
img3 = Image.open('deletebutton.jpeg')
resize_img3 = img3.resize((300,80))
buttonImg2 = ImageTk.PhotoImage(resize_img3)
B2 = Button(app,command=callback2,bg="#1B7358" ,image = buttonImg2,borderwidth=0)
B2.grid(row=1,rowspan=150,column=0)
#addbutton3
img4 = Image.open('takeattendance.jpeg')
resize_img4 = img4.resize((300,80))
buttonImg3 = ImageTk.PhotoImage(resize_img4)
B3 = Button(app,bg = '#1B7358' ,image = buttonImg3,borderwidth=0,command=take)
B3.grid(row=2,rowspan=275,column=0)
#-----------------------------------------
def on_enterB1(a):
    global updatedImage
    newImg = Image.open(r'AddWhite.jpeg')
    resize_new = newImg.resize((300,80))
    updatedImage = ImageTk.PhotoImage(resize_new)
    B1.configure(image = updatedImage)

def on_leaveB1(a):
    global updatedImage
    newImg = Image.open(r'addbutton.jpeg')
    resize_new = newImg.resize((300,80))
    updatedImage = ImageTk.PhotoImage(resize_new)
    B1.configure(image = updatedImage)
def on_enterB2(a):
    global updatedImage2
    newImg = Image.open(r'AddDel.png')
    resize_new = newImg.resize((300,80))
    updatedImage2 = ImageTk.PhotoImage(resize_new)
    B2.configure(image = updatedImage2)

def on_leaveB2(a):
    global updatedImage2
    newImg = Image.open(r'deletebutton.jpeg')
    resize_new = newImg.resize((300,80))
    updatedImage2 = ImageTk.PhotoImage(resize_new)
    B2.configure(image = updatedImage2)


def on_enterB3(a):
    global updatedImage3
    newImg = Image.open(r'takeWhite.png')
    resize_new = newImg.resize((300,80))
    updatedImage3= ImageTk.PhotoImage(resize_new)
    B3.configure(image = updatedImage3)


def on_leaveB3(a):
    global updatedImage3
    newImg = Image.open(r'takeattendance.jpeg')
    resize_new = newImg.resize((300,80))
    updatedImage3 = ImageTk.PhotoImage(resize_new)
    B3.configure(image = updatedImage3)

B1.bind('<Enter>',on_enterB1)
B1.bind('<Leave>',on_leaveB1)

B2.bind('<Enter>',on_enterB2)
B2.bind('<Leave>',on_leaveB2)

B3.bind('<Enter>',on_enterB3)
B3.bind('<Leave>',on_leaveB3)
#-------------------------------------------


app.mainloop()
