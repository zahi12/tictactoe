# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:39:51 2019

@author: pierr
"""

import random
from Game_Final import Game
            
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
    if player.win_game(player):
        print("victoire de "+ str(player.symbol))
    
    