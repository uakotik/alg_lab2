from tkinter import *
with open("DS1.txt", "r")as f:
    r=Tk();
    r.geometry("960x540")
    r.title("LAB2")
    canvas = Canvas(r, height=540, width=960)
    canvas.pack()
    for line in f:
        i=line.split(" ")
        y=int(i[0])
        x=int(i[1])
        canvas.create_line(x,y,x+1,y+1)
    r.mainloop()