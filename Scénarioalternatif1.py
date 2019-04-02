# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:39:51 2019

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
        self.players=[]
        self.first_player=None
        self.current_player=None
        self.last_case=None
    
    def get_board(self): #crée le plateau
        return self.board 
        
    def get_current_player(self): #détermine le joueur qui doit jouer
        self.players=[self.player1,self.player2]
        if self.move_number==0:
            tirage_au_sort=[0,1]
            if random.choice(tirage_au_sort) == 0 :
                self.first_player=self.players[0]
                self.current_player=self.players[0]
                return self.current_player
            self.current_player=self.players[1]
            return self.current_player
        else :
            if game.move_number%2 == 0 :
                self.current_player=self.first_player
                return self.current_player
            else :
                for i in [0,1] :
                    player =self.players[i]
                    if player.get_symbol() != self.first_player.get_symbol() :
                        self.current_player=self.players[i]
                        return self.current_player
        
    def end_draw(self):
        print("Draw!") #affichage du résultat

    def end_win(self):
        winner = self.get_current_player().symbol
        print("Well done,", winner,"You Win!") #affichage du résultat        
          
                          
    
        
        
        
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
                if case.case_is_full() :
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
        grid_position=self.get_grid_position()
        for i in range (1,4):
            for j in range (1,4) :
                case_position = (i,j)
                case = board.get_case(grid_position,case_position)
                if not case.case_is_full():
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
        self.playable_grid=[]
    
    def play(self, grid_position, case_position):
        case = board.get_case(grid_position,case_position)
        case.owner = game.current_player.symbol #le symbol de la case devient le symbol du joueur
        game.last_case = case_position #la dernière case jouée devient cette case
        if self.draw_grid(grid_position):
            grid=board.get_grid(grid_position)
            grid.owner = 0         
        if self.win_grid(grid_position): 
            grid=board.get_grid(grid_position)
            grid.owner = game.get_current_player().symbol        
        if self.draw_game():
            game.draw_end()
        if self.win_game():
            game.end_win()         
        game.move_number+=1
        

    def get_symbol(self):
        return self.symbol
    
    def get_playable_grid(self): 
        playable_grid=[]
        if game.move_number == 0 :#premier coup
            for i in range (1,4) :
                for j in range (1,4) :
                    playable_grid.append((i,j))
            return playable_grid #renvoie toutes les grilles  
        grid = board.get_grid(game.last_case)
        if grid.grid_is_full()  :
            print (1)
            for i in range (9):
                    if board.grids[i].grid_is_full == False :
                        playable_grid.append(board.grids[i].get_grid_position)
            return playable_grid
        else :
            playable_grid.append(game.last_case)
            return playable_grid #renvoie une liste de (a,b) qui correspondent aux grilles jouables 
        
    
    def win_line(self,grid_position):
        for i in range (1,4):
            a=0
            for j in range (1,4):
                case = board.get_case(grid_position, (i,j))
                player = game.current_player
                if case.owner == player.symbol :
                    a+=1
            if a == 3 : 
                return True
        return False

    def win_column(self,grid_position):
        for j in range (1,4):
            a=0
            for i in range (1,4):
                case = board.get_case(grid_position, (i,j))
                player = game.current_player
                if case.owner == player.symbol :
                    a+=1
            if a == 3 : 
                return True
        return False
    

    def win_diagonal(self,grid_position):
        a=0
        b=0
        for i in range (1,4):   #test si la premiere diagonale est remplie
            case = board.get_case(grid_position, (i,i))
            player = game.current_player           
            if case.owner == player.symbol :
                a+=1
    
        for case_position in [(3,1),(2,2),(1,3)]: #test si l'autre diagonale est remplie
            case = board.get_case(grid_position,case_position)
            player = game.current_player           
            if case.owner == player.symbol :
                b+=1
        
        if a==3 or b==3:
            return True
        return False

        
    def win_grid(self,grid_position):
        if self.win_line(grid_position) or self.win_column(grid_position) or self.win_diagonal(grid_position):
            return True
        else:
            return False
        
    def draw_grid(self,grid_position):
        grid=board.get_grid(grid_position)
        if grid.grid_is_full() and not self.win_grid(grid_position):
            return True
        return False
   
    def win_COLUMN(self):
        for j in range (1,4):
            a=0
            b=0
            for i in range (1,4):
                grid = board.get_grid(grid_position = (i,j))
                player = game.current_player                
                if grid.owner == player.symbol :
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
                grid = board.get_grid(grid_position=(i,j))
                player = game.current_player
                if grid.owner == player.symbol :
                    a+=1
                if grid.owner == 0 :
                    b+=1
            if a+b == 3 and b!=3 : 
                return True
        return False

    def win_DIAGONAL(self):
        a=0
        b=0
        c=0
        d=0
        for i in range (1,4): #test la premiere diagonal
            grid = board.get_grid(grid_position = (i,i))
            player = game.current_player
            if grid.owner == player.symbol :
                a+=1
            if grid.owner == 0 :
                b+=1
       
        for grid_position in[(3,1),(2,2),(1,3)]: #test la deuxieme diagonal
            grid = board.get_grid(grid_position)
            player = game.current_player
            if grid.owner == player.symbol :
                c+=1
            if grid.owner == 0 :
                d+=1
            
        if (a+b==3 and b!=3) or (c+d==3 and d!=3) :
            return True
        return False 
    
    def win_game(self):
        if self.win_LINE() or self.win_COLUMN() or self.win_DIAGONAL():
            return True
        else:
            return False
        
    def draw_game(self):
        a=0
        for i in range(1,4):
            for j in range (1,4):
                grid = board.get_grid(grid_position = (i,j))
                if grid.owner == 0 :
                    a+=1
                if a==9:
                    return True
        return False
    
            
if __name__ == "__main__": 
    game = Game()
    game.start()
    board = game.get_board()
    if not board.is_empty : 
        raise Exception("jeu vide")
 
    print("1er coup : Le premier joueur joue")    
    
    player = game.get_current_player() #joueur 1 avant de jouer (premier coup)
    
    if player.symbol != 1:
        raise Exception("Ce n'est pas une vraie erreur, simplement je veux que dans ce scénario, le joueur 1 commence donc il faut relancer le scénario jusqu'à ce que le random(choice de game.get_current_player() tire le numéro 0")                                    #on vérifie le symbole
    
    player.play(grid_position = (2,2), case_position = (2, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,2), case_position = (1, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,1), case_position = (1, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,1), case_position = (2, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,2), case_position = (2, 3)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,3), case_position = (1, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,1), case_position = (3, 3)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (3,3), case_position = (1, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,1), case_position = (3, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (3,2), case_position = (3, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (3,2), case_position = (2, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,2), case_position = (2, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,1), case_position = (1, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,1), case_position = (3, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (3,1), case_position = (3, 3)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (3,3), case_position = (2, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,2), case_position = (3, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (3,1), case_position = (2, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,2), case_position = (1, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,2), case_position = (3, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (3,1), case_position = (1, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,1), case_position = (2, 3)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,3), case_position = (2, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,2), case_position = (3, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (3,2), case_position = (1, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,1), case_position = (1, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,2), case_position = (2, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    
    player.play(grid_position = (2,2), case_position = (1, 3)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,3), case_position = (2, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,2), case_position = (3, 3)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (3,3), case_position = (2, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,1), case_position = (2, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    """grid full"""


    player.play(grid_position = (1,1), case_position = (2, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,1), case_position = (1, 2)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,2), case_position = (1, 3)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,3), case_position = (1, 1)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    
    player.play(grid_position = (1,1), case_position = (1, 3)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (1,3), case_position = (2, 3)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    player.play(grid_position = (2,3), case_position = (3, 3)) # joueur 1 joue (premier coup)
    player = game.get_current_player() # joueur 2 avant de jouer
    
    """Victoire"""
    
    player.play(grid_position = (3,3), case_position = (3, 3)) # joueur 1 joue (premier coup)
    
    
    