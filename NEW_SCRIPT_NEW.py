# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:36:47 2019

@author: User
"""

import random

PLAYER_CIRCLE = 1
PLAYER_CROSS = 2
move_number=0  
    
case_positon=()
grid_position=()


class Game (): #début du jeu
    def __init__(self):
        pass
    
    def start(self):   #crée les objets
        self.board = Board()
        self.player1=Player(PLAYER_CIRCLE,[],[])
        self.player2=Player(PLAYER_CROSS,[],[])
    
    def get_board(self): #crée le plateau
        return self.board 
        
    def get_current_player(self): #détermine le joueur qui doit jouer
        if move_number==0:
            players=[self.player1,self.player2]
            first_player=None
            tirage_au_sort=[i for i in range (2)]
            if random.choice(tirage_au_sort) == 0 :
                first_player=players[0]
                return first_player
            first_player=players[1]
            return first_player
        else :
            if move_number%2 == 0 :
                return first_player
            else :
                for i in players :
                    if players[i] != first_player:
                        return players[i]
        
        
        
class Board(): #Le plateau de jeu entier
    def __init__(self):
        self.grids = []
        for i in range(1,4):
            for j in range (1,4) :
                self.grids.append(Grid(i,j)) #crée les 9 grilles

    def get_grid(self,grid_position) :
        for i in range (9):
            if self.grids[i].get_grid_position() == grid_position :
                return self.grids[i]

    def get_case (self,grid_position,case_position) : #sélectionne/donne accès à la case à ces coordonnées
        grid = self.get_grid(grid_position) #on sélectionne la grille à la grid_position
        case = grid.get_case(case_position) #on sélectionne la case à la case_position dans la grid
        return case
    
    def is_empty(self) : #teste si le plateau est vide
        for i in range (9) :
            grid=self.grids[i]
            for j in range(9):
                case=grid.cases[j]
                if case.case_is_full :
                    return False
        return True            
    
    def clean_board(self):
        for i in range (9) :
            grid=self.grids[i]
            for j in range(9):
                case=grid.cases[j]
                if case.case_is_full :
                    case.owner=None
        
        
            
class Grid() : #La grille 3x3
    def __init__(self,line,column) :
        self.grid_position=(line,column)
        self.cases=[]
        for i in range (1,4):
            for j in range (1,4):
                case_position = (i,j)
                self.cases.append(Case(case_position))
                
    def get_grid_position (self):
        return self.grid_position
    
    def get_case(self,case_position):
        return Case(case_position)
    
    def grid_is_full (self) : #teste si la grille est pleine
        for i in range (1,4):
            for j in range (1,4) :
                if not case_is_full:
                    return False
        return True        
    
        
class Case (): #la case simple
    def __init__(self,case_position) :
        self.case_position=case_position
        self.owner = None     

    def case_is_full(self) : #teste si la case est pleine (jouée)
        if self.owner == None :
            return False
        return True

        
        
class Player() : 
    def __init__(self,symbol,plays_list,winning_grid_list) :
        self.symbol=symbol
        self.plays_list=plays_list #tableau
        self.winning_grid_list=winning_grid_list
    
    def play(self, grid_position, case_position): 
        board.get_case(grid_position,case_position).owner = game.get_current_player#le symbol de la case devient le symbol du joueur
        self.plays_list.append([grid_position,case_position])
        last_case=[case_position] #la dernière case jouée devient cette case

    
    def get_playable_grid(self): 
        playable_grid=[]
        grid = board.get_grid(last_case)
        if move_number == 0 :  #premier coup
            for i in range (1,10) :
                for j in range (1,10) :
                    playable_grid.append(i,j)
                    return playable_grid #renvoie toutes les grilles  
        elif grid.grid_is_full  :
            for i in range (9):
                    if board.grids[i].grid_is_full == False :
                        playable_grid.append(board.grids[i].get_grid_position)
        else :
            playable_grid.append(last_case)
            return playable_grid #renvoie une liste de (a,b) qui correspondent aux grilles jouables 
    
    def get_case_position(self,grid_position):
        T=[] #sert a stocker les positions des cases qui nous interesse en lui precisant la position de la grille.
        for X in self.plays_list:
           if X[0]==grid_position:  
               T.append(X[1]) #recupere toutes les cases joues par un  joueur .
        return T
    
    def win_line(self,grid_position):
        T=self.get_case_position(grid_position)
        print(T)
        a=0 #compteur
        for x in range(1,4):
            a=0
            for X in T:
                if (X==(x,1) or X==(x,2) or X==(x,3))and(a!=3): #qd a==3 cest inutile
                    a+=1
            if a==3:
                return True
        return False
    def win_column(self,grid_position):
        T=self.get_case_position(grid_position)
        a=0    #compteur
        for y in range(1,4):
            a=0
            for X in T:
                if (X==(1,y) or X==(2,y) or X==(3,y))and(a!=3): #qd a==3 cest inutile
                    a+=1
            if a==3:
                return True
        return False
    
    def win_diagonal(self,grid_position):
        T=self.get_case_position(grid_position)
        a=0
        for y in range(1,4):
            a=0
            for X in T:
                if (X==(1,1) or X==(2,2) or X==(3,3))and(a!=3): #qd a==3 cest inutile
                    a+=1
            if a==3:
                return True
        return False   
   
    def get_winning_grid(self,grid_position):
        if self.win_line(grid_position) or self.win_couloumn(grid_position) or self.win_diagonal(grid_position):
            return self.winning_grid_list.append(grid_position)
        else:
            return False
   
    def win_COLUMN(self):
        a=0   #compteur
        for x in range(1,4):
           a=0
           for X in self.winning_grid_list:
               if (X==(x,1) or X==(x,2) or X==(x,3))and(a!=3) :
                   a+=1
           if a==3:
               return True
        return False
    
    def win_LINE(self):
        a=0    #compteur
        for y in range(1,4):
            a=0
            for X in self.winning_grid_list:
                if (X==(1,y) or X==(2,y) or X==(3,y))and(a!=3): 
                    a+=1
            if a==3:
                return True
        return False

    def win_DIAGONAL(self):
        a=0    #compteur
        for y in range(1,4):
            a=0
            for X in self.winning_grid_list  :
                if (X==(1,1) or X==(2,2) or X==(3,3))and(a!=3):
                    a+=1
            if a==3:
                return True
        return False 
    
    def winning_game(self):
        if self.win_LINE() or self.win_COLUMN() or self.win_DIAGONAL():
            return True
        else:
            return False
    
            
if __name__ == "__main__": 
    game = Game()
    game.start()
    board = game.get_board()
    if not board.is_empty : 
        print ("pas vide")
    
    
    player = game.get_current_player() #joueur 1 avant de jouer (premier coup)
    
    player.play(grid_position = (1, 1), case_position = (2, 3)) # joueur 1 joue (premier coup)
    if board.get_case((1,1),(2,3)).owner != PLAYER_CIRCLE:
        raise "Erreur, on attendait un rond dans la case 2,3 de la grille 1,1"
        
    player = game.get_current_player() # joueur 2 avant de jouer
    if player.symbol != PLAYER_CROSS:                                     #on vérifie le symbole
        raise "Erreur, on attendait le joueur Croix"
    if player.get_playable_grid() != [(2, 3)]:                            #la grille de jeu
        raise "Erreur, on attendait comme grille jouable la grille 2,3"	
            
    player.play(grid_position=(2,3), case_position = (1,3))  #le joueur joue
    
    if board.get_case(grid=(2,3), case=(1,2)):
        print("a")
    if player.grid_is_winning() :                                  #la victoire de great grid
        grid.property = player.name
        grid.grid_is_full = True 
    if player.get_victory() :                                             #la victoire totale
        game.win()    
    if player.get_draw_great_grid() :                                     #l'égalité sur great grid
        grid.grid_is_full = True
    if player.get_draw():                                                 #égalité totale
        game.draw ()

    if grid.grid_is_full(player.get_playable_grid()) :          ##mettre un changement de joueur à la fin de la fonction
        player.get_playable_grid.grid.grid_is_empty()