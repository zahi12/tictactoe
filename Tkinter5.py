# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:41:12 2019

@author: pierr
"""
import tkinter
import Scénario4

"""class Tkinter_Game(): 
    classe qui fait le lien entre IHM et Game
    def __init__(self):
        pass 
    
    def Tk_Cliquer(self):
        player.play(Tkinter_Graph.grid_position,Tkinter_Graph.case_position)
        self.Tk_Win()
        self.Tk_Draw()
        
    def Tk_Win():
        if player.win_game:
            win=tkinter.Label(Tkinter_Graph.fenetre, text= game.get_current_player() + "a gagné")
            
    def Tk_Draw():
        if player.draw_game():
            draw=Label(Tkinter_Graph.fenetre, text= "Draw !")"""
    
            
            
class Tkinter_Graph():  #IHM
    """Notre IHM 
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    def __init__(self):
        self.fenetre=tkinter.Tk()
        
        self.start_clic = 0
        
        # Création de nos widgets
        self.welcome = tkinter.Label(self.fenetre, text="Vous allez jouer au Morpion version Expert ! (2 joueurs)")
        self.welcome.pack()
        
        self.bouton_quitter = tkinter.Button(self.fenetre, text="Quitter", command=self.end)
        self.bouton_quitter.pack(side="left")
        
        self.bouton_jouer = tkinter.Button(self.fenetre, text="Jouer", fg="red", command=self.cliquer)
        self.bouton_jouer.pack(side="right")
        
        self.ecriture=("comic sans ms",13)
        self.nbcase=9
        self.grid_position=()
        self.case_position=()
        self.case_side=50
        self.x0=9
        self.y0=9
        self.chiffre=[0,1,2,3,4,5,6,7,8,9]
            
    def cliquer(self):
        """Il y a eu un clic sur le bouton.
        On change la valeur du label message."""
        
        self.start_clic +=1
        if self.start_clic == 1 :
            self.welcome["text"] = "C'est parti !"
        elif self.start_clic == 2 :
            self.welcome.destroy()
            self.bouton_jouer.destroy()
            
            self.cadre=tkinter.Frame(self.fenetre)
            self.cadre.pack()
            self.can=tkinter.Canvas(self.cadre, height=500,width=500,bg="white")
            self.can.bind("<Button-1>",self.donne_position)
            self.TexteC=tkinter.Text(self.fenetre,height=25,width=25)

            
            self.titel=tkinter.Label(self.fenetre, text="Tic Tac Toe", fg="red")
            
            self.can.pack(side="left")
            self.titel.pack(side="top")  

            self.grille()                     
        else : 
            pass
        
    def end (self):
        self.fenetre.quit()
        self.fenetre.destroy()
 
    def grille (self):
        for i in range(self.nbcase+1):
            if i%3==0:
                self.can.create_line(self.x0+self.case_side*i, self.y0,self.x0+self.case_side*i,self.y0 + self.nbcase*self.case_side)
                self.can.create_line(self.x0, self.y0+self.case_side*i,self.x0+self.nbcase*self.case_side ,self.y0+self.case_side*i)
            else :
                self.can.create_line(self.x0+self.case_side*i, self.y0,self.x0+self.case_side*i,self.y0 + self.nbcase*self.case_side,fill="blue")
                self.can.create_line(self.x0, self.y0+self.case_side*i,self.x0+self.nbcase*self.case_side, self.y0+self.case_side*i,fill="blue")
            
    def get_grid_position(self,event):
        for i in range (0,3):
            for j in range(0,3):
                if event.x<159+150*j and event.x>9+150*j and event.y<159+i*150 and event.y>9+150*i:
                    self.grid_position=(i+1,j+1)
                    return(self.grid_position)
                
    def get_case_position(self,event):
        for i in range (0,9):
            for j in range(0,9):
                if event.x<59+50*j and event.x>9+50*j and event.y<59+i*50 and event.y>9+50*i:
                    self.case_position=(i%3+1,j%3+1)
                    return(self.case_position)
                
    
    def donne_position(self,event):
        self.TexteC.delete("0.0",tkinter.END)# on efface l'écriture précédente
        self.grid_position=self.get_grid_position(event)
        self.case_position=self.get_case_position(event)
        self.can.create_oval(event.x,event.y,(event.x+30),(event.y+30),fill="red",outline="blue")  
        self.TexteC.insert(tkinter.END,"grid_position="+str(grid_position)+"\ncase_position="+str(case_position))

    def correspond(x,y):
        return [x,y]
 


IHM=Tkinter_Graph()

IHM.fenetre.mainloop()
