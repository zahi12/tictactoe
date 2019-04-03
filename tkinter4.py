# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:40:49 2019

@author: User
"""

from tkinter import*
from random import*
ecriture=("comic sans ms",13)
nbcase=9
grid_position=()
case_position=()
case_side=50
x0,y0=9,9
chifre=[0,1,2,3,4,5,6,7,8,9]
 
def fin ():
    fenetre.quit()
    fenetre.destroy()
 
def grille():
    for i in range(nbcase+1):
        if i%3==0:
            Can.create_line(x0+case_side*i, y0,x0+case_side*i,y0 + nbcase*case_side)
            Can.create_line(x0, y0+case_side*i,x0+nbcase*case_side ,y0+case_side*i)
        else:
            Can.create_line(x0+case_side*i, y0,x0+case_side*i,y0 + nbcase*case_side,fill="blue")
            Can.create_line(x0, y0+case_side*i,x0+nbcase*case_side ,y0+case_side*i,fill="blue")
            
def get_grid_position(event):
    for i in range (0,3):
        for j in range(0,3):
            if event.x<159+150*j and event.x>9+150*j and event.y<159+i*150 and event.y>9+150*i:
                grid_position=(i+1,j+1)
                return(grid_position)
                
def get_case_position(event):
    for i in range (0,9):
        for j in range(0,9):
           if event.x<59+50*j and event.x>9+50*j and event.y<59+i*50 and event.y>9+50*i:
               case_position=(i%3+1,j%3+1)
               return(case_position)
                
            
    
    
def donne_position(event):
    TexteC.delete("0.0",END)# on efface l'écriture précédente
    grid_position=get_grid_position(event)
    case_position=get_case_position(event)
    Can.create_oval(event.x,event.y,(event.x+30),(event.y+30),fill="red",outline="blue")  
    TexteC.insert(END,"grid_position="+str(grid_position)+"\ncase_position="+str(case_position))
 
 
 
def jouer(event):
    global trouve
    [i,j]=correspond(event.x,event.y)
    if i in range(nb) and j in range (nb):   # on ne fait rien si le click est hors grille
        Can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=coul(i,j))

def correspond(x,y):
    return [x,y]
 

fenetre=Tk()
Cadre=Frame(fenetre)
Texte1=Label(fenetre,text="TIC TAC TOE",fg="red",font=ecriture)
BouttonQuit=Button(fenetre,text="quitter", command=fin)
BouttonJouer=Button(fenetre,text="jouer", command=grille)
TexteC=Text(fenetre,height=25,width=25)
Can=Canvas(Cadre,height=500,width=500,bg="white")

 

Texte1.grid(row=0,column=0)
BouttonQuit.grid(row=50, column=100)
Cadre.grid(row=1,column=0)
Can.grid(row=2, column=0)
BouttonJouer.grid(row=0, column=50)
TexteC.grid(row=1, column=3)
 
Can.bind("<Button-1>",donne_position)
 
fenetre.mainloop()