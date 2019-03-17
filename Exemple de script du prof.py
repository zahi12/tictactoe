PLAYER_CIRCLE = 1
PLAYER_CROSS = 2
move_number=0  
class Game ():
    def __init__(self):
        pass
    
    def start(self):
        self.board = Board()
        self.player= Player()
    
    def get_board(self):
        return self.board
    
    def get_current_player(self):
        return self.current_player 
        
        
        
class Board():
    def __init__(self):
        self.grids = []
        for i in range(9):
            self.grids.append(Grid())
            
    def get_grid(self, x, y):
        return self.grids.append((x,y))
    
    def is_empty(self) :
        for i in range (self.grids) :
            if case.on :
                return False
        return True    
        
            
class Grid() :
    def __init__(self) :
        pass
    
class Player() :
    def __init__(self, Name) :
        self.Name= Name
    
    def get_playable_grid(self):
        if move_number=0 :  
            for i in range (1,10) :
                for j in range (1,10) :
                    return ([i,j])
        else :
            
    

if __name__ == "__main__":
    game = Game()
    game.start()
    board = game.get_board()
    if not board.is_empty():
        raise "Erreur, la grille n'est pas vide"
    player = game.get_current_player()
    if player.symbol != PLAYER_CIRCLE:
        raise "Erreur, on attendait le joueur Rond"
    player.play(position_great_grid = (1, 1), position_little_grid = (2, 3))
    if board.get_grid(1, 1).get_case(2, 3).symbol != PLAYER_CIRCLE:
        raise "Erreur, on attendait un rond dans la case 2,3 de la grille 1,1"
    player = game.get_current_player()
    if player.symbol != PLAYER_CROSS:
        raise "Erreur, on attendait le joueur Croix"
    if player.get_playable_grid() != [(2, 3)]:
        raise "Erreur, on attendait comme grille jouable la grille 2,3"	
    if player.get_victory_great_grid() :
        grid.property = player
        grid.grid_is_full = True
    if player.get_victory() :
        game.win()    
    if player.get_draw_great_grid() :
        grid.great_grid_is_full = True
    if player.get_draw():
        game.draw ()
    player.play(position_great_grid=(2,3), position_little_grid = (1,3))
    if player.get_playable_grid() == grid.little_grid_is_full() :
        player.get_playable_grid () = grid.little_grid_is_empty()
#....




