from gtts import gTTS
import os
import wikipedia
import tkinter
from tkinter import PhotoImage
from playsound import playsound


root =tkinter.Tk()
img=PhotoImage(file="wikipic.png")
img1=PhotoImage(file="python.png")
frame = tkinter.Frame(root,
                        bg="lightblue",
                        height=200)


frame.pack(fill=tkinter.X)
canvas=tkinter.Canvas(frame, width=1600,height=200)
canvas.place(x=0,y=0)
canvas.create_image(500,50, image=img1, anchor= 'nw')

frame2=tkinter.Frame(root,
                    bg="lightgreen",
                    height=650, width=600)

frame2.pack(fill=tkinter.X)

label=tkinter.Label(frame, text="text to speech using",
                        font="italic,60",
                        bg="white")

label.place(x=750,y=50)
label1=tkinter.Label(frame,text="SEARCH TO GET A SUMMARY FROM WIKIPEDIA ",
                    font="bold,30",
                    bg="#e6e8e6")
label1.place(x=600,y=0)

canvas=tkinter.Canvas(frame2, width=1600,height=650)
canvas.place(x=0,y=0)
canvas.create_image(50,50, image=img, anchor= 'nw')


entry=tkinter.Entry(frame2,
                    width=45,
                    bd= 4,font=45)
entry.place(x=550,y=50)
entry.insert(0,"")



#search fron wikipedia
def play():
    srch=wikipedia.summary(entry.get())
    op=gTTS(text=srch,lang='en',slow=False)
    op.save("op.mp3")
    path='op.mp3'
    playsound(path)
    os.remove('op.mp3')
    os.kill()
    
    

    

def playtext():
    op=gTTS(text=entry.get(),
            lang="en",
            slow=False)
    op.save("op.mp3")
    path='op.mp3'
    playsound(path)
    os.remove('op.mp3')
    
    
    

button2=tkinter.Button(frame2,text="speech",
            width="15", pady=10,
            font="bold,15",
            command=playtext,bg="yellow")

button2.place(x=600,y=150)

#button3=tkinter.Button(frame2,text="stop",
 #          fornt="bold,15",command=stop,bg="yellow")

#button3.pla(x=750,y=0)

button=tkinter.Button(frame2, text = "Search",
			width = "15", pady = 10,
			font = "italic, 15",
			command = play, bg='yellow')

button.place(x=800,y=150)

button3=tkinter.Button(frame2,text="QUIT",
                        width=10,pady=10,
                        command=quit,bg="yellow")
button3.place(x=750,y=250)

root.geometry("1500x1000")

root.mainloop()

                 