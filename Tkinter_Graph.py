# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:45:03 2019

@author: pierr
"""

import tkinter
from Game import Game        
            
class Tkinter_Graph():  #IHM
    #Notre IHM 
    #Tous les widgets sont stockés comme attributs de cette fenêtre.
    def __init__(self):
        self.fenetre=tkinter.Tk()
        self.game=Game()
        
        self.start_clic = 0
        
        # Création de nos widgets
        self.welcome = tkinter.Label(self.fenetre, text="Vous allez jouer au Morpion version Expert ! (2 joueurs)")
        self.welcome.grid(row=0,column=5)
        
        self.bouton_quitter = tkinter.Button(self.fenetre, text="Quitter", command=self.end)
        self.bouton_quitter.grid(row=5, column=0)
        
        self.bouton_jouer = tkinter.Button(self.fenetre, text="Jouer", fg="red", command=self.cliquer)
        self.bouton_jouer.grid(row=5, column=10)
        
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
            self.cadre.grid(row=1,column=0)
            self.can=tkinter.Canvas(self.cadre, height=500,width=500,bg="white")
            self.TexteC=tkinter.Text(self.fenetre,height=25,width=33)
            self.can.bind("<Button-1>",self.play_event)
            
            self.titel=tkinter.Label(self.fenetre, text="Tic Tac Toe", fg="red")
            
            self.can.grid(row=2,column=0)
            self.titel.grid(row=0,column=0)  
            self.TexteC.grid(row=1,column=3)
            self.grille()   
            
            self.game.start()
            self.board=self.game.get_board()
            
            self.first_move()
            
    def first_move(self):
        self.TexteC.delete("0.0",tkinter.END)               # on efface l'écriture précédente
        self.TexteC.insert(tkinter.END,"Vous pouvez jouer dans n'importe quelle grille."+"\n Le joueur "+str(self.game.first_player.symbol)+" commence."+"\n Bon jeu !")


    def play_event(self,event):
        self.grid_position=self.get_grid_position(event)
        self.case_position=self.get_case_position(event)
        player = self.game.get_current_player()
        playable_grid=player.get_playable_grid()
        if not self.case_position==None :
            print(player.symbol)
            print(self.game.board.get_case(self.grid_position,self.case_position).owner)
            if self.grid_position in playable_grid :
                if self.game.board.get_case(self.grid_position,self.case_position).owner == None :
                    player.play(self.grid_position,self.case_position)
                    print(self.game.board.get_case(self.grid_position,self.case_position).owner)
                    
               
                    if player.symbol==1:
                        self.can.create_oval(self.debut_case_x,self.debut_case_y,self.fin_case_x,self.fin_case_y,fill="red",outline="blue")
                   
                    if player.symbol==2:
                        self.can.create_oval(self.debut_case_x,self.debut_case_y,self.fin_case_x,self.fin_case_y,fill="blue",outline="blue")
                       
                    if player.win_game():
                        self.fenetre_fin=tkinter.Tk()
                        self.win = tkinter.Label(self.fenetre_fin, text= "Le joueur "+str(self.game.current_player.symbol)+" a gagné !!!")
                        self.win.grid(row=0,column=5)
                            
                        self.bouton_fin = tkinter.Button(self.fenetre_fin, text="Terminé", command=self.end_all)
                        self.bouton_fin.grid(row=5, column=0)
                            
                    if player.draw_game():
                        self.fenetre_fin=tkinter.Tk()
                        self.draw = tkinter.Label(self.fenetre_fin, text= "Egalité parfaite !!!")
                        self.draw.grid(row=0,column=5)
                        
                        self.bouton_fin = tkinter.Button(self.fenetre_fin, text="Terminé", command=self.end_all)
                        self.bouton_fin.grid(row=5, column=0)
                    
                    player = self.game.get_current_player()
                    playable_grid=player.get_playable_grid()
                    self.TexteC.delete("0.0",tkinter.END)               # on efface l'écriture précédente
                    self.TexteC.insert(tkinter.END,"grilles jouables : "+str(playable_grid))
                else:
                    pass
            else :
                pass
        else: 
            pass

           
         
        
        
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
                if  9+150*j<event.x and event.x<159+150*j and 9+150*i<event.y and event.y<159+i*150 :
                    self.grid_position=(i+1,j+1)
                    return(self.grid_position)
                
    def get_case_position(self,event):
        self.debut_case_x=9    #vont être utiliser plus tard dans la méthode "donne_position"
        self.fin_case_x=59
        self.debut_case_y=9
        self.fin_case_y=59
        for i in range (0,9):
            for j in range(0,9):
                if self.debut_case_x+50*j<event.x and event.x<self.fin_case_x+50*j and self.debut_case_y+50*i<event.y and event.y<self.fin_case_y+i*50:
                    self.case_position=(i%3+1,j%3+1)
                    self.debut_case_x=self.debut_case_x+50*j
                    self.fin_case_x=self.fin_case_x+50*j
                    self.debut_case_y=self.debut_case_y+50*i
                    self.fin_case_y=self.fin_case_y+50*i
                    return(self.case_position)
                
    
    
    def correspond(x,y):
        return [x,y]
 
    def end (self):
        self.fenetre.quit()
        self.fenetre.destroy()

    def end_all(self):
        self.fenetre_fin.quit()      
        self.fenetre_fin.destroy        
        self.fenetre.quit()
        self.fenetre.destroy()
        
IHM=Tkinter_Graph()
IHM.fenetre.mainloop()