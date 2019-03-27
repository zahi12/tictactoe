# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:25:25 2019

@author: pierr
"""

import random


class Game (): #début du jeu
    def __init__(self):
        pass
    
    def start(self):   #crée les objets
        self.board = Board()
        self.player1=Player(1)
        self.player2=Player(2)
        self.move_number=0
    
    def get_board(self): #crée le plateau
        return self.board 
        
    def get_current_player(self): #détermine le joueur qui doit jouer
        self.players=[self.player1,self.player2]
        first_player=None
        if self.move_number==0:
            tirage_au_sort=[i for i in range (2)]
            if random.choice(tirage_au_sort) == 0 :
                first_player=self.players[0]
                return first_player
            first_player=self.players[1]
            return first_player
        else :
            if game.move_number%2 == 0 :
                return first_player
            else :
                for i in [0,1] :
                    if self.players[i].symbol != first_player.symbol:
                        return self.players[i]
        
        
        
class Board(): #Le plateau de jeu entier
    def __init__(self):
        self.grids = []
        for i in range(1,4):
            for j in range (1,4) :
                grid_position=(i,j)
                self.grids.append(Grid(grid_position)) #crée les 9 grilles

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
            grid.owner = None
            for j in range(9):
                case=grid.cases[j]
                if case.case_is_full :
                    case.owner=None
        
        
            
class Grid() : #La grille 3x3
    def __init__(self,grid_position) :
        self.owner=None
        self.grid_position=grid_position
        self.cases=[]
        for i in range (1,4):
            for j in range (1,4):
                case_position = (i,j)
                self.cases.append(Case(case_position))
                
    def get_grid_position (self):
        return self.grid_position
    
    def get_case(self,case_position):
        for i in range (9):
            case = self.cases[i]
            if case.get_case_position() == case_position:
                return case
    
    def grid_is_full (self) : #teste si la grille est pleine
        for i in range (1,4):
            for j in range (1,4) :
                case_position = (i,j)
                case = board.get_case(case_position)
                if not case.case_is_full:
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
    
    def get_case_position(self) :
        return self.case_position

        
        
class Player() : 
    def __init__(self,symbol) :
        self.symbol=symbol
        self.last_case=None
    
    def play(self, grid_position, case_position):
        case = board.get_case(grid_position,case_position)
        case.owner = game.get_current_player().symbol #le symbol de la case devient le symbol du joueur
        self.last_case=case_position #la dernière case jouée devient cette case
        game.move_number+=1

    
    def get_playable_grid(self): 
        playable_grid=[]
        grid = board.get_grid(self.last_case)
        if game.move_number == 0 :  #premier coup
            for i in range (1,10) :
                for j in range (1,10) :
                    playable_grid.append(i,j)
                    return playable_grid #renvoie toutes les grilles  
        elif grid.grid_is_full  :
            for i in range (9):
                    if board.grids[i].grid_is_full == False :
                        playable_grid.append(board.grids[i].get_grid_position)
                        return playable_grid
        else :
            playable_grid.append(self.last_case)
            return playable_grid #renvoie une liste de (a,b) qui correspondent aux grilles jouables 
        
    
    def win_line(self,grid_position):
        for i in range (1,4):
            a=0
            for j in range (1,4):
                case = board.get_case(grid_position, (i,j))
                if case.owner == game.get_current_player.symbol :
                    a+=1
            if a == 3 : 
                return True
        return False

    def win_column(self,grid_position):
        for j in range (1,4):
            a=0
            for i in range (1,4):
                case = board.get_case(grid_position, (i,j))
                if case.owner == game.get_current_player.symbol :
                    a+=1
            if a == 3 : 
                return True
        return False
    

    def win_diagonal(self,grid_position):
        a=0
        for i in range (1,4):
            case = board.get_case(grid_position, (i,i))
            if case.owner == game.get_current_player.symbol :
                a+=1
        if a==3 :
            return True
        return False

        
    def win_grid(self,grid_position):
        if self.win_line(grid_position) or self.win_column(grid_position) or self.win_diagonal(grid_position):
            grid = board.get_grid(grid_position)
            grid.owner = game.get_current_player.symbol
            return True
        else:
            return False
        
    def draw_grid(self,grid_position):
        grid=board.get_grid(grid_position)
        if grid.grid_is_full and not self.win_grid(grid_position):
            grid.owner=0
            return True
        return False
   
    def win_COLUMN(self):
        for j in range (1,4):
            a=0
            b=0
            for i in range (1,4):
                grid = board.get_grid(i,j)
                if grid.owner == game.get_current_player.symbol :
                    a+=1
                if grid.owner == 0 :
                    b+=1
            if a+b == 3 and b!=3 : 
                return True
        return False
    
    def win_LINE(self):
        for i in range (1,4):
            a=0
            b=0
            for j in range (1,4):
                grid = board.get_grid(i,j)
                if grid.owner == game.get_current_player.symbol :
                    a+=1
                if grid.owner == 0 :
                    b+=1
            if a+b == 3 and b!=3 : 
                return True
        return False

    def win_DIAGONAL(self):
        a=0
        b=0
        for i in range (1,4):
            grid = board.get_grid(i,i)
            if grid.owner == game.get_current_player.symbol :
                a+=1
            if grid.owner == 0 :
                b+=1
        if a+b==3 and b!=3 :
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
        raise Exception("jeu vide")
    
    player = game.get_current_player() #joueur 1 avant de jouer (premier coup)
    
    player.play(grid_position = (1, 1), case_position = (2, 3)) # joueur 1 joue (premier coup)
    if board.get_case((1,1),(2,3)).owner != 1:
        print(board.get_case((1,1),(2,3)).owner)
        raise Exception("Erreur, on attendait un rond dans la case 2,3 de la grille 1,1")
        
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 2:                                     #on vérifie le symbole
        print(player.symbol)
        print(game.move_number)
        raise Exception("Erreur, on attendait le joueur Croix")
    if player.get_playable_grid() != [(2, 3)]:                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 2,3")	
            
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
        
        
        
        
        #il faut la notion de propiete de la case seulement sur la case