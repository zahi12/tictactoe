# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:45:03 2019

@author: pierr
"""
import pygame
import tkinter
from Game2 import Game    

pygame.init()
            
class Tkinter_Graph():  #IHM
    #Notre IHM 
    #Tous les widgets sont stockés comme attributs de cette fenêtre.
    def __init__(self):
        self.window=tkinter.Tk()
        self.game=Game()
        
        self.start_clic = 0
        
        # Création de nos widgets
        self.welcome = tkinter.Label(self.window, text="Vous allez jouer au Morpion version Expert ! commecer par indiquer vos nom (2 joueurs)", fg = "black" )
        self.welcome.grid(row=0,column=5)
        
        self.exit_button = tkinter.Button(self.window, text="Quitter", command=self.end)
        self.exit_button.grid(row=20, column=0)
        
        self.play_button = tkinter.Button(self.window, text="Jouer", fg="red", command=self.cliquer)
        self.play_button.grid(row=20, column=10)
        
        self.get_player_name()

        self.ecriture=("comic sans ms",13)
        self.nbcase=9
        self.grid_position=()
        self.case_position=()
        self.case_side=50
        self.x0=9
        self.y0=9
        self.chiffre=[0,1,2,3,4,5,6,7,8,9]
        
    def get_player_name(self):    
        self.player1_name=tkinter.StringVar()
        self.player2_name=tkinter.StringVar()
        self.entry1=tkinter.Entry(self.window,textvariable=self.player1_name,width=30)
        self.entry2=tkinter.Entry(self.window,textvariable=self.player2_name,width=30)
        self.entry1.insert(0,"nom 1 ")
        self.entry2.insert(0,"nom 2")
        self.entry1.grid(row=5, column=5)
        self.entry2.grid(row=5, column=10)

    def cliquer(self):
        """Il y a eu un clic sur le bouton.
        On change la valeur du label message."""
        self.start_clic+=1
          
        
        if self.start_clic == 1 :
            self.entry1.destroy()
            self.entry2.destroy()
            self.play_button.destroy()
            self.welcome["text"] = "Choisissez votre univers !"
            
            self.get_options()
            self.display_options()
            
        elif self.start_clic == 2 :
            self.destroy_starting_buttons()
            
            self.get_tk_board()
            self.display_tk_board()
            self.display_tictactoe_grid()   
            
            self.game.start()
            self.board=self.game.get_board()
            
            self.first_move()
            self.can.bind("<Button-1>",self.play_event)
            
  
    def get_tk_board(self):
        self.cadre=tkinter.Frame(self.window)
        self.cadre.grid(row=1,column=0)
        self.can=tkinter.Canvas(self.cadre, height=500,width=500,bg=self.can_bg)
        self.TexteC=tkinter.Text(self.window,height=25,width=33)
        self.titel=tkinter.Label(self.window, text="Tic Tac Toe", fg=self.titel_fg, bg=self.titel_bg)
        
    def display_tk_board(self):
        self.can.grid(row=2,column=0)
        self.titel.grid(row=0,column=0)  
        self.TexteC.grid(row=1,column=3)
    
    def display_tictactoe_grid (self):
        for i in range(self.nbcase+1):
            if i%3==0:
                self.can.create_line(self.x0+self.case_side*i, self.y0,self.x0+self.case_side*i,self.y0 + self.nbcase*self.case_side, fill=self.grille_big_lines)
                self.can.create_line(self.x0, self.y0+self.case_side*i,self.x0+self.nbcase*self.case_side ,self.y0+self.case_side*i, fill=self.grille_big_lines)
            else :
                self.can.create_line(self.x0+self.case_side*i, self.y0,self.x0+self.case_side*i,self.y0 + self.nbcase*self.case_side,fill=self.grille_little_lines)
                self.can.create_line(self.x0, self.y0+self.case_side*i,self.x0+self.nbcase*self.case_side, self.y0+self.case_side*i,fill=self.grille_little_lines)
        
    def first_move(self):
        self.TexteC.delete("0.0",tkinter.END)               # on efface l'écriture précédente
        self.TexteC.insert(tkinter.END,"Vous pouvez jouer dans n'importe quelle grille."+"\n"+str(self.get_current_player_name())+" commence."+"\n Bon jeu !")

    def play_event(self,event):
        self.grid_position=self.get_grid_position(event)
        self.case_position=self.get_case_position(event)
        player = self.game.get_current_player()
        case=self.game.board.get_case(self.grid_position,self.case_position)
        playable_grid=player.get_playable_grid()
        
        if (not self.case_position==None) and (self.grid_position in playable_grid) and (case.owner == None) : #si on ne clique pas sur les bords, que la grille est jouable et que la case n'est pas jouée
                        
            player.play(self.grid_position,self.case_position)                        
               
            self.display_player_symbol()

            if player.win_game():
                self.display_win()
                            
            if player.draw_game():
                self.display_draw()
                    
            player = self.game.get_current_player()
            playable_grid=player.get_playable_grid()
            self.TexteC.delete("0.0",tkinter.END)               # on efface l'écriture précédente
            self.TexteC.insert(tkinter.END,"le tour de "+str(self.get_current_player_name())+"\ngrilles jouables : "+str(playable_grid))                
        
        else: 
            pass
    
    def display_player_symbol(self):
        player = self.game.get_current_player()
        if player.symbol==1:
            self.can.create_oval(self.debut_case_x,self.debut_case_y,self.fin_case_x,self.fin_case_y,fill=self.player1_symbol,outline="black")
                   
        if player.symbol==2:
            self.can.create_line(self.debut_case_x,self.debut_case_y,self.fin_case_x,self.fin_case_y, fill = self.player2_symbol, width=3)
            self.can.create_line(self.debut_case_x,self.fin_case_y,self.fin_case_x,self.debut_case_y, fill = self.player2_symbol, width=3)



    def display_win(self): 
        self.end_window=tkinter.Tk()
        self.win = tkinter.Label(self.end_window, text=str(self.get_current_player_name())+" a gagné !!!")
        self.win.grid(row=0,column=5)
        self.display_end()
        
        
    def display_draw(self):
        self.end_Window=tkinter.Tk()
        self.draw = tkinter.Label(self.end_Window, text= "Egalité parfaite !!!")
        self.draw.grid(row=0,column=5)
        self.display_end()
       
    def display_end(self):
        self.end_button = tkinter.Button(self.end_Window, text="Terminé", command=self.end_all)
        self.end_button.grid(row=5, column=0)
    
            
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
                    
    def get_current_player_name(self):
        player=self.game.current_player
        if player.symbol==1 :
            return self.player1_name.get()
        if player.symbol==2 :
            return self.player2_name.get()
                
    def get_options (self):
        self.button_past=tkinter.Button(self.window, text=" Passé ", command=self.past)
        self.button_present=tkinter.Button(self.window, text=" Présent ", command=self.present)
        self.button_future=tkinter.Button(self.window, text=" Futur ", command=self.future)
        self.button_disco=tkinter.Button(self.window, text=" Disco! ", command=self.disco)
        
        self.past_option=False
        self.present_option=False
        self.future_option=False
        self.disco_option=False
        
    
    def past (self):
        self.past_option=True
        self.can_bg="grey"
        self.titel_fg="white"
        self.titel_bg="grey"
        self.grille_little_lines= "dark grey"
        self.grille_big_lines="white"
        self.player1_symbol="dark green"
        self.player2_symbol="black"
        self.medieval_music=pygame.mixer.Sound("Epic Celtic Battle Music - Battle For Camelot (Tartalo Music).wav")
        self.medieval_music.play()
        
        self.cliquer()
        
    def present (self):
        self.present_option=True
        self.can_bg="yellow"
        self.titel_fg="red"
        self.titel_bg="yellow"
        self.grille_little_lines="orange"
        self.grille_big_lines="red"
        self.player1_symbol="magenta"
        self.player2_symbol="grey"  
        self.funk_music=pygame.mixer.Sound("The Chemical Brothers - Got To Keep On (Official Video).wav")
        self.funk_music.play()

        self.cliquer()
        
    def future (self) :
        self.future_option=True
        self.can_bg="black"
        self.titel_fg="cyan"
        self.titel_bg="black"
        self.grille_little_lines="cyan"
        self.grille_big_lines="white"
        self.player1_symbol="blue"
        self.player2_symbol="white"        
        self.interstellar_music=pygame.mixer.Sound("Interstellar - Main Theme - Hans Zimmer.wav")
        self.interstellar_music.play()

        self.cliquer()
        
    def disco (self):
        self.disco_option=True
        self.can_bg="pink"
        self.titel_fg="orange"
        self.titel_bg="pink"
        self.grille_little_lines="cyan"
        self.grille_big_lines="yellow"
        self.player1_symbol="green"
        self.player2_symbol="magenta"  
        self.born_to_be_alive=pygame.mixer.Sound("Patrick Hernandez - Born to be Alive (Climax original motion picture soundtrack).wav")
        self.born_to_be_alive.play()
        
        self.cliquer()

    def display_options (self):
        self.button_past.grid(row=1,column=0)
        self.button_present.grid(row=1,column=5)
        self.button_future.grid(row=1,column=10)
        self.button_disco.grid(row=1, column=16)
        
    def destroy_starting_buttons(self):
        self.welcome.destroy()
        self.play_button.destroy()
        self.button_past.destroy()
        self.button_present.destroy()
        self.button_future.destroy()
        self.button_disco.destroy()
    
    def correspond(x,y):
        return [x,y]
 
    def end (self):
        self.window.quit()
        self.window.destroy()
        if self.past_option:
            self.medieval_music.stop()
        if self.present_option:
            self.funk_music.stop()
        if self.future_option:
            self.interstellar_music.stop()
        if self.disco_option:
            self.born_to_be_alive.stop()
        
    def end_all(self):
        self.end_window.quit()      
        self.end_window.quit()
        self.end_Window.destroy()
        self.window.destroy()
        if self.past_option:
            self.medieval_music.stop()
        if self.present_option:
            self.funk_music.stop()
        if self.future_option:
            self.interstellar_music.stop()
        if self.disco_option:
            self.born_to_be_alive.stop()

        
IHM=Tkinter_Graph()
IHM.window.mainloop()