import tkinter as tk
from tkinter import *
from tkinter import filedialog
from colors import color
from random import randint
from graph import prim ,kruskal
from read import lengthg
def save_file():
    open_file=open("graph.txt","w")
   
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()
def clear():
        for widget in frame.winfo_children():
               widget.destroy()
def show_frame(frame):
    frame.tkraise()

    frame.tkraise()
def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)

def createline(x1,y1,x2,y2,canvasName,col):
    return canvasName.create_line(x1,y1,x2,y2,fill=col)
def createlabel(x1,y1,string,canvasName,col):
    label1 = Label(canvasName, text=string ,fg=col)
    label1.place(x=x1,y=y1)
def createlabel1(x1,y1,string,canvasName,col):
    label1 = Label(canvasName, text=string ,fg=col,font=("Arial",14))
    label1.place(x=x1,y=y1)    
def nb(n,t):
    nbn=0
    for i in range(lengthg()):
        if(t[n][i]!=0):
            nbn+=1
    return nbn
window = tk.Tk()

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.geometry("1000x600")
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)

for frame in (frame1, frame2):
    frame.grid(row=0,column=0,sticky='nsew')
def fr2(frame,algo):
    clear()
    myCanvas = tk.Canvas(frame, width=1000,height = 600)
    myCanvas.pack()
    col=color(lengthg())

    x1=100
    y2=170
    k=[]
    if (algo=="prim"):
        al=prim()
        t=al[0]
    else :
        al=kruskal()
        t=al[0]
    for i in range(lengthg()):
      n=nb(i,t)
      k.append([x1,y2])
      if(i==1):
          x1=x1+90
          y2=y2
      else:
          if(i%2==0):
              x1+=90
              y2+=90
          else:
              x1+=90
              y2-=90
    createlabel1(400,10,algo,myCanvas,"red")
    for i in range(lengthg()):
        create_circle(k[i][0],k[i][1],20, myCanvas)
    for i in range(lengthg()):
        for j in range(lengthg()):
            if(t[i][j]!=0):
                createline(k[i][0]+20,k[i][1],k[j][0]-20,k[j][1],myCanvas,col[j])
                if(nb(i,t)==2):
                    createlabel((k[j][0]+k[i][0])/2,(k[j][1]+k[i][1])/2,t[i][j],myCanvas,col[j])
                else:
                    createlabel((k[j][0]+k[i][0])/2,15+(k[j][1]+k[i][1])/2,t[i][j],myCanvas,col[j])

                
    for i in range(lengthg()):
        createlabel(k[i][0]-10,k[i][1]-10,str(i),myCanvas,"black")
    tex="cout minimale avec l'algorithme de "+algo+" ="+str(int(al[1]))
    createlabel1(250,500,tex,myCanvas,"red")
    btn=Button(myCanvas,text="Home",font=("Arial",12) ,command=lambda:show_frame(frame1))
    btn.place(x=400,y=550)
    frame.tkraise()



label1 = Label(frame1, text="Remplir la Matrice d'adg dans la zone de text et cliquez save file\n apres choisir l'algorithme ")
label1.place(x=600,y=100)
b1=Button(frame1,text="save file"  , command=save_file)
b1.place(x=10,y=10)
b2=Button(frame1,text="  prim  ",font=("Arial",16) ,command=lambda:fr2(frame2,"prim") )
b2.place(x=700,y=300)
b3=Button(frame1,text="kruskal",font=("Arial",16),command=lambda:fr2(frame2,"Kruskal"))
b3.place(x=700,y=200)
entry =Text(frame1 , height=33 , width= 58,wrap=WORD)
entry.place(x=10,y=50)

show_frame(frame1)

window.mainloop()
