PLAYER_CIRCLE = 1
PLAYER_CROSS = 2
move_number=0  
    
class Game (): #début du jeu
    def __init__(self):
        pass
    
    def start(self):   #crée les objets
        self.board = Board()
        self.player= Player()
    
    def get_board(self): #crée le plateau
        return self.board
    
    def get_current_player(self): #détermine le joueur qui doit jouer
        return self.current_player 
        
        
        
class Board(): #Le plateau de jeu entier
    def __init__(self):
        self.grids = []
        for i in range(9):
            self.grids.append(Grid()) #crée les 9 grilles

    def get_grid(self,grid_position) :
        return 

    def get_case (self,grid_position,case_position) : #sélectionne/donne accès à la case à ces coordonnées
        grid = self.get_grid(grid_position) #on sélectionne la grille à la grid_position
        return grid.get_case(case_position) #on sélectionne la case à la case_position dans la grid
    
    def is_empty(self) : #teste si le plateau est vide
        for i in range (len(self.grids)) :
            if Grid.grid_is_full :
                return False
            return True    
        
            
class Grid() : #La grille 3x3
    def __init__(self) :
        pass
        
    def grid_is_full (grid_position) : #teste si la grille est pleine
        pass
    
    def get_grid(grid_position):
        return board.get_grid(grid_position)
        
        
class Case (): #la case simple
    def __init__(self) :
        self.owner=0        

    def case_is_full() : #teste si la case est pleine (jouée)
        pass
        
        
class Player() : 
    def __init__(self) :
        self.Name= PLAYER_CIRCLE
    
    def play(self, grid, case): 
        Case.SYMBOL=self.get_current_player.symbol #le smbol de la case devient le symbol du joueur
        last_case=[(a,b),(x,y)] #la dernière case jouée devient cette case
    
    def get_playable_grid(self): 
        playable_grid=[]
        if move_number == 0 :  #premier coup
            for i in range (1,10) :
                for j in range (1,10) :
                    playable_grid.append(i,j)
                    return playable_grid #renvoie toutes les grilles  
        else :
            playable_grid.append(last_case)
            return playable_grid #renvoie une liste de (a,b) qui correspondent aux grilles jouables 
            
if __name__ == "__main__": 
    game = Game()
    game.start()
    board = game.get_board()
    if not board.is_empty():
        raise "Erreur, la grille n'est pas vide"
    player = game.get_current_player() #joueur 1 avant de jouer (premier coup)
    if player.symbol != PLAYER_CIRCLE:
        raise "Erreur, on attendait le joueur Rond"
    player.play(position_grid = (1, 1), position_case = (2, 3)) # joueur 1 joue (premier coup)
    if board.get_case((1,1),(2,3)).symbol != PLAYER_CIRCLE:
        raise "Erreur, on attendait un rond dans la case 2,3 de la grille 1,1"
        
    player = game.get_current_player() # joueur 2 avant de jouer
    if player.symbol != PLAYER_CROSS:                                     #on vérifie le symbole
        raise "Erreur, on attendait le joueur Croix"
    if player.get_playable_grid() != [(2, 3)]:                            #la grille de jeu
        raise "Erreur, on attendait comme grille jouable la grille 2,3"	
            
    player.play(position_grid=(2,3), position_case = (1,3))  #le joueur joue
    if board.get_case(grid=(2, 3), case=(1, 2)):
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
    if player.get_playable_grid() == grid.grid_is_full() :          ##mettre un changement de joueur à la fin de la fonction
        player.get_playable_grid. grid.grid_is_empty()
#....




