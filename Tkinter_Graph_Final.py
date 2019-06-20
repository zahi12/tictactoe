# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:55:50 2019

@author: pierr
"""

import pygame
import tkinter
from Game_Final import Game    

pygame.init()
            
class Tkinter_Graph():  #IHM
    #Notre IHM 
    #Tous les widgets sont stockés comme attributs de cette fenêtre.
    def __init__(self):
        self.window=tkinter.Tk()
        self.game=Game()
        
        self.start_clic = 0
        
        # Création de nos widgets
        self.welcome = tkinter.Label(self.window, text="Vous allez jouer au Morpion version Expert ! Commencez par indiquer vos noms (2 joueurs)", fg = "black" )
        self.welcome.grid(row=0,column=2)
        
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
        self.entry1.insert(0,"Nom du joueur 1 ")
        self.entry2.insert(0,"Nom du joueur 2")
        self.entry1.grid(row=5, column=0)
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
        self.Text_left=tkinter.Text(self.window,height=15,width=33)
        self.Text_right=tkinter.Text(self.window, height=15, width=38)
        self.titel=tkinter.Label(self.window, text="Tic Tac Toe", fg=self.titel_fg, bg=self.titel_bg)
        
    def display_tk_board(self):
        self.can.grid(row=2,column=5)
        self.titel.grid(row=0,column=0)  
        self.Text_left.grid(row=1,column=1)
        self.Text_right.grid(row=1,column=2)
    
    def display_tictactoe_grid (self):
        for i in range(self.nbcase+1):
            if i%3==0:
                self.can.create_line(self.x0+self.case_side*i, self.y0,self.x0+self.case_side*i,self.y0 + self.nbcase*self.case_side, fill=self.grille_big_lines)
                self.can.create_line(self.x0, self.y0+self.case_side*i,self.x0+self.nbcase*self.case_side ,self.y0+self.case_side*i, fill=self.grille_big_lines)
            else :
                self.can.create_line(self.x0+self.case_side*i, self.y0,self.x0+self.case_side*i,self.y0 + self.nbcase*self.case_side,fill=self.grille_little_lines)
                self.can.create_line(self.x0, self.y0+self.case_side*i,self.x0+self.nbcase*self.case_side, self.y0+self.case_side*i,fill=self.grille_little_lines)
        
    def first_move(self):
        self.Text_left.delete("0.0",tkinter.END)               # on efface l'écriture précédente
        if self.past_option : 
            self.Text_left.insert(tkinter.END,"Oye Oye, jeunes mécréants !"+"\nLe roi souhaite observer votre querelle ! Vous pouvez jouer dans n'importe quelle grille. Le plus brave d'entre vous pourrait même gagner moult avoine pour son cheval ! "+"\n"+str(self.get_current_player_name())+" commence."+"\n Querellez !")
            
        elif self.present_option:
            self.Text_left.insert(tkinter.END,"Bienvenue à nos 2 joueurs."+"\nLe premier joueur peut jouer dans n'importe quelle grille"+"\n"+str(self.get_current_player_name())+" commence."+"\n Bon jeu !")
            
        elif self.future_option:
            self.Text_left.insert(tkinter.END," *voix robotique* Bien le bonjour, êtres humains."+"\nLa première créature peut jouer dans n'importe quelle grille. L'entité la plus avancée pourrait même repartir avec tous les films <<Hunger Game>> ! HA HA HA "+"\n"+str(self.get_current_player_name())+" commence."+"\n Que la Force soit avec vous!")
            
        elif self.disco_option:
            self.Text_left.insert(tkinter.END,"C'est DISCO TIME ! "+"\nLe premier danseur peut jouer dans n'importe quelle grille. Le plus <<disco>> d'entre vous pourrait même repartir avec un magnifique pantalon patte d'eph !"+"\n"+str(self.get_current_player_name())+" commence."+"\n Let's dance !")
        
        elif self.reggae_option:
            self.Text_left.insert(tkinter.END,"Bienvenue man ! "+"\nOn est ici pour jouer tranquille, le premier rastafari qui joue peut jouer dans n'importe quelle grille. Le plus cool de vous deux pourraient même gagner un disque dédicacé de Bob Marley "+"\n"+str(self.get_current_player_name())+" commence."+"\n Peace !")
        
        elif self.french_option:
            self.Text_left.insert(tkinter.END,"Ramenez la coupe à la maison ! "+"\nLe sportif qui engage peut jouer dans n'importe quelle grille du terrain ! Le meilleur d'entre vous pourrait même gagner le short que portait Zidane !"+"\n"+str(self.get_current_player_name())+" commence."+"\n Et l'arbitre donne le coup d'envoi !")
        
        elif self.libanese_option:
            self.Text_left.insert(tkinter.END,"mrhbana bik fi 2 laeibayna. "+"\nyumkin lilaeib al'awal allaeb fi 'ayi shabakatin."+"\n"+str(self.get_current_player_name())+" yabda "+"\n Yallah !")

            
        elif self.hardcore_option :
            self.Text_left.insert(tkinter.END,"Bienvenue en mode Hardcore. "+"\nLe premier joueur a gagné une grille remporte la partie. Vous pouvez jouer dans n'importe quelle grille"+"\n"+str(self.get_current_player_name())+" commence."+"\n Bon jeu !")
        
            
            
    def play_event(self,event):
        self.grid_position=self.get_grid_position(event)
        self.case_position=self.get_case_position(event)
        player = self.game.get_current_player()
        grid=self.board.get_grid(self.grid_position)
        case=self.game.board.get_case(self.grid_position,self.case_position)
        playable_grid=player.get_playable_grid()
        if (not self.case_position==None) and (self.grid_position in playable_grid) and (case.owner == None) and (grid.owner==None): #si on ne clique pas sur les bords, que la grille est jouable et que la case n'est pas jouée
            player.play(self.grid_position,self.case_position)                        
            self.display_player_symbol()
            
            if player.win_grid(self.grid_position, player):
                self.display_win_grid(player)
                if self.hardcore_option :
                    self.display_win_hardcore(player)
                
              
            if player.draw_grid(self.grid_position):
                self.display_draw_grid()

            if player.win_game(player):
                self.display_win(player)
                            
            if player.draw_game():
                self.display_draw()
                    
            player = self.game.get_current_player()
            playable_grid=player.get_playable_grid()
            self.Text_left.delete("0.0",tkinter.END)               # on efface l'écriture précédente
            self.Text_left.insert(tkinter.END,"\nC'est au tour de "+str(self.get_current_player_name())+"\nGrilles jouables : "+str(playable_grid))       
        
        else: 
            pass
    
    def display_player_symbol(self):
        player = self.game.get_current_player()
        if player.symbol==1:
            self.can.create_oval(self.debut_case_x,self.debut_case_y,self.fin_case_x,self.fin_case_y,fill=self.player1_symbol,outline="black")
                   
        if player.symbol==2:
            self.can.create_line(self.debut_case_x,self.debut_case_y,self.fin_case_x,self.fin_case_y, fill = self.player2_symbol, width=3)
            self.can.create_line(self.debut_case_x,self.fin_case_y,self.fin_case_x,self.debut_case_y, fill = self.player2_symbol, width=3)

    def display_win_grid(self,player):
        if player.symbol==1 :
            self.Text_right.insert(tkinter.END,"\n"+str(self.player1_name.get())+" a remporté la grille "+str(self.grid_position))
        else :
            self.Text_right.insert(tkinter.END,"\n"+str(self.player2_name.get())+" a remporté la grille "+str(self.grid_position))

    def display_draw_grid(self):
        if self.hardcore_option :
            self.Text_right.insert(tkinter.END,"\nEgalité dans la grille "+str(self.grid_position)+"\nLa partie est serrée !")
        else :    
            self.Text_right.insert(tkinter.END,"\nEgalité dans la grille "+str(self.grid_position)+"\nLes 2 joueurs remportent donc cette grille")
        
    def display_win(self,player): 
        self.end_window=tkinter.Tk()
        if player.symbol==1:
            self.win = tkinter.Label(self.end_window, text=str(self.player1_name.get())+" a gagné !!!")
        else :
            self.win = tkinter.Label(self.end_window, text=str(self.player2_name.get())+" a gagné !!!")
        self.display_end()
        self.desactivate_all()
        
       
    def display_win_hardcore(self,player): 
        self.end_window=tkinter.Tk()
        if player.symbol==1:
            self.win = tkinter.Label(self.end_window, text=str(self.player1_name.get())+" a gagné en mode Hardcore!!!")
        else :
            self.win = tkinter.Label(self.end_window, text=str(self.player2_name.get())+" a gagné en mode Hardcore!!!")
        self.display_end()
        self.desactivate_all()        
        
    def desactivate_all(self):
        for i in range (9):
            grid=self.board.grids[i]
            for j in range(9):
                case=grid.cases[j]
                case.case_is_full=True                
        
    def display_draw(self):
        self.end_window=tkinter.Tk()
        self.draw = tkinter.Label(self.end_window, text= " Egalité parfaite !!! ")
        self.draw.grid(row=0,column=5)
        self.display_end()
       
    def display_end(self):
        self.end_button = tkinter.Button(self.end_window, text=" Terminé ", command=self.end_all)
        self.end_button.grid(row=5, column=5)
        self.win.grid(row=0,column=5)
                    
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
        self.button_reggae=tkinter.Button(self.window, text=" Reggae ", command=self.reggae)
        self.button_french=tkinter.Button(self.window, text=" 1998/2018 ", command=self.french)
        self.button_libanese=tkinter.Button(self.window, text=" Liban ", command=self.libanese)
        self.button_hardcore=tkinter.Button(self.window, text=" Mode Hardcore ", command=self.hardcore)
        
        self.past_option=False
        self.present_option=False
        self.future_option=False
        self.disco_option=False
        self.reggae_option=False
        self.french_option=False
        self.libanese_option=False
        self.hardcore_option=False
        
        
        
    
    def past (self):
        self.past_option=True
        self.can_bg="grey"
        self.titel_fg="white"
        self.titel_bg="grey"
        self.grille_little_lines= "dark grey"
        self.grille_big_lines="white"
        self.player1_symbol="dark green"
        self.player2_symbol="black"
        self.medieval_music=pygame.mixer.Sound("1.wav")
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
        self.funk_music=pygame.mixer.Sound("2.wav")
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
        self.interstellar_music=pygame.mixer.Sound("3.wav")
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
        self.born_to_be_alive=pygame.mixer.Sound("4.wav")
        self.born_to_be_alive.play()
        
        self.cliquer()
        
    def reggae (self):
        self.reggae_option=True
        self.can_bg="yellow"
        self.titel_fg="red"
        self.titel_bg="green"
        self.grille_little_lines="green"
        self.grille_big_lines="red"
        self.player1_symbol="green"
        self.player2_symbol="dark green"  
        self.reggae_music=pygame.mixer.Sound("5.wav")
        self.reggae_music.play()
        
        self.cliquer()    
        
    def french (self):
        self.french_option=True
        self.can_bg="blue"
        self.titel_fg="white"
        self.titel_bg="blue"
        self.grille_little_lines="white"
        self.grille_big_lines="red"
        self.player1_symbol="white"
        self.player2_symbol="dark red"  
        self.french_music=pygame.mixer.Sound("6.wav")
        self.french_music.play()
        
        self.cliquer()
        
    def libanese (self):
        self.libanese_option=True
        self.can_bg="white"
        self.titel_fg="red"
        self.titel_bg="white"
        self.grille_little_lines="red"
        self.grille_big_lines="green"
        self.player1_symbol="red"
        self.player2_symbol="green"  
        self.libanese_music=pygame.mixer.Sound("7.wav")
        self.libanese_music.play()
        
        self.cliquer()        
        
    def hardcore (self):
        self.hardcore_option = True
        self.can_bg="white"
        self.titel_fg="black"
        self.titel_bg="white"
        self.grille_little_lines= "dark grey"
        self.grille_big_lines="black"
        self.player1_symbol="red"
        self.player2_symbol="orange"
        
        self.cliquer()
        
    def display_options (self):
        self.button_past.grid(row=1,column=2)
        self.button_present.grid(row=2,column=2)
        self.button_future.grid(row=3,column=2)
        self.button_disco.grid(row=4, column=2)
        self.button_reggae.grid(row=5,column=2)
        self.button_french.grid(row=6,column=2)
        self.button_libanese.grid(row=7,column=2)
        self.button_hardcore.grid(row=8,column=2)
        
    def destroy_starting_buttons(self):
        self.welcome.destroy()
        self.play_button.destroy()
        self.button_past.destroy()
        self.button_present.destroy()
        self.button_future.destroy()
        self.button_disco.destroy()
        self.button_reggae.destroy()
        self.button_french.destroy()
        self.button_libanese.destroy()
        self.button_hardcore.destroy()
    
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
        if self.reggae_option:
            self.reggae_music.stop()
        if self.french_option:
            self.french_music.stop()
        if self.libanese_option:
            self.libanese_music.stop()
        
    def end_all(self):
        self.window.quit()      
        self.end_window.quit()
        self.window.destroy()
        self.end_window.destroy()
        if self.past_option:
            self.medieval_music.stop()
        if self.present_option:
            self.funk_music.stop()
        if self.future_option:
            self.interstellar_music.stop()
        if self.disco_option:
            self.born_to_be_alive.stop()
        if self.reggae_option:
            self.reggae_music.stop()
        if self.french_option:
            self.french_music.stop()
        if self.libanese_option:
            self.libanese_music.stop()            

        
IHM=Tkinter_Graph()
IHM.window.mainloop()