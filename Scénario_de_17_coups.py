# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 00:25:19 2019

@author: pierr
"""

import random
from Game_Final import Game

    
 
if __name__ == "__main__": 
    game=Game()
    board=game.get_board()
 
    print("1er coup : Le premier joueur joue")    
    
    player = game.get_current_player() #joueur 1 avant de jouer (premier coup)
    
    if player.symbol != 1:
        raise Exception("Ce n'est pas une vraie erreur, simplement je veux que dans ce scénario, le joueur 1 commence donc il faut relancer le scénario jusqu'à ce que le random(choice de game.get_current_player() tire le numéro 0")                                    #on vérifie le symbole
    
    player.play(grid_position = (1, 1), case_position = (2, 3)) # joueur 1 joue (premier coup)
    
    print("player", board.get_case(grid_position = (1, 1), case_position = (2, 3)).owner, "a la case jouée")
    
    if board.get_case(grid_position=(1,1),case_position=(2,3)).owner != 1:
        raise Exception("Erreur, on attendait le joueur 1 dans la grille 1,1 et case 2,3")
    
    for i in range (9) :            #cette boucle correspond à un affichage des cases jouées, c'est pour pouvoir suivre le déroulement du scénario
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position())
                
    print("\n2eme coup :Le deuxième joueur joue")       
    player = game.get_current_player() # joueur 2 avant de jouer
    
        
    if player.symbol != 2:                                             #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 2") 
    if not (2,3) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 2,3")	
    
    player.play(grid_position=(2,3), case_position = (1,1))  #le joueur joue
    
    print("owner de la grid (2,3):",board.get_grid((2,3)).owner)         #pour surveiller l'état des "owner")
    print("owner de la case (1,1) de la grille (2,3):",board.get_case((2,3),(1,1)).owner)
    
    if board.get_case(grid_position=(2,3), case_position=(1,1)).owner != 2:
        raise Exception("Erreur, on attendait le joueur 2  dans la grille 2,3 et case  1,1")
           
    if player.win_grid(grid_position = (2,3), player=player):                                 #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (2,3)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")  
     
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position()) 
    
    print("\n3eme coup :Le premier joueur joue")    
    player = game.get_current_player() # joueur 1 avant de jouer
    
    if player.symbol != 1:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 1")       
    if not (1,1) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille (1,1)")	    
        
    player.play(grid_position=(1,1), case_position = (2,2))  #le joueur joue

    if board.get_case(grid_position=(1,1), case_position=(2,2)).owner != 1:
        raise Exception("Erreur, on attendait le joueur 1 dans la grille 1,1 et la case 2,2")
       
    if player.win_grid(grid_position = (1,1),player=player) :                                  #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (1,1)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")                        
        
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position())
             
    print("\n4eme coup :Le deuxième joueur joue")       
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 2:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 2")
    if not (2,2) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 2,2")	
        
    player.play(grid_position=(2,2), case_position = (1,1))  #le joueur joue
    if board.get_case(grid_position=(2,2), case_position=(1,1)).owner != 2:
        raise Exception("Erreur, on attendait un X dans la grille 2,2 et la case 1,1")
        
    if player.win_grid(grid_position = (1,1),player=player) :                                  #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (2,3)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")                        
    
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position()) 

    print("\n5eme coup :Le premier joueur joue")                
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 1:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 1")
    if not (1,1) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 1,1")	
        
    player.play(grid_position=(1,1), case_position = (2,1))  #le joueur joue
    if board.get_case(grid_position=(1,1), case_position=(2,1)).owner != 1:
        raise Exception("Erreur, on attendait le joueur 1 dans la grille 1,1 et case 2,1")
    
    if not player.win_grid(grid_position = (1,1),player=player) :                                  #la victoire de grid
        raise Exception("on est censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (1,1)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")
                        
    
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position())
    
    print("\n6eme coup :Le deuxième joueur joue")       
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 2:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 2")
    if not (2,1) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 2,1")	
        
    player.play(grid_position=(2,1), case_position = (3,3))  #le joueur joue
    if board.get_case(grid_position=(2,1), case_position=(3,3)).owner != 2:
        raise Exception("Erreur, on attendait un X dans la grille 2,1 et la case 3,3")
        
    if player.win_grid(grid_position = (2,1),player=player) :                                  #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (2,1)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")                        
    
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position()) 
    
    print("\n7eme coup :Le premier joueur joue")                
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 1:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 1")
    if not (3,3) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 3,3")	
        
    player.play(grid_position=(3,3), case_position = (3,2))  #le joueur joue
    if board.get_case(grid_position=(3,3), case_position=(3,2)).owner != 1:
        raise Exception("Erreur, on attendait le joueur 1 dans la grille 3,3 et case 3,2")
    
    if player.win_grid(grid_position = (3,3),player=player) :                                  #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (3,3)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")
                        
    
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position())
                
    
    print("\n8eme coup :Le deuxième joueur joue")       
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 2:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 2")
    if not (3,2) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 3,2")	
        
    player.play(grid_position=(3,2), case_position = (3,3))  #le joueur joue
    if board.get_case(grid_position=(3,2), case_position=(3,3)).owner != 2:
        raise Exception("Erreur, on attendait un X dans la grille 3,2 et la case 3,3")
        
    if player.win_grid(grid_position = (3,2),player=player) :                                  #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (3,2)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")                        
    
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position()) 
                
    print("\n9eme coup :Le premier joueur joue")                
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 1:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 1")
    if not (3,3) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 3,3")	
        
    player.play(grid_position=(3,3), case_position = (2,2))  #le joueur joue
    if board.get_case(grid_position=(3,3), case_position=(2,2)).owner != 1:
        raise Exception("Erreur, on attendait le joueur 1 dans la grille 3,3 et case 2,2")
    
    if player.win_grid(grid_position = (3,3),player=player) :                                  #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (3,3)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")
        
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position()) 
                
    print("\n10eme coup :Le deuxième joueur joue")       
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 2:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 2")
    if not (2,2) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 2,2")	
        
    player.play(grid_position=(2,2), case_position = (3,3))  #le joueur joue
    if board.get_case(grid_position=(2,2), case_position=(3,3)).owner != 2:
        raise Exception("Erreur, on attendait un X dans la grille 2,2 et la case 3,3")
        
    if player.win_grid(grid_position = (2,2),player=player) :                                  #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (2,2)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")                        
    
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position()) 
                
       
    print("\n11eme coup :Le premier joueur joue")                
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 1:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 1")
    if not (3,3) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 3,3")	
        
    player.play(grid_position=(3,3), case_position = (1,2))  #le joueur joue
    if board.get_case(grid_position=(3,3), case_position=(1,2)).owner != 1:
        raise Exception("Erreur, on attendait le joueur 1 dans la grille 3,3 et case 1,2")
    
    if not player.win_grid(grid_position = (3,3),player=player) :                                  #la victoire de grid
        raise Exception("on est censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (3,3)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")
        
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position()) 
                
                
    print("\n12eme coup :Le deuxième joueur joue")       
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 2:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 2")
    if not (1,2) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 1,2")	
        
    player.play(grid_position=(1,2), case_position = (2,2))  #le joueur joue
    if board.get_case(grid_position=(1,2), case_position=(2,2)).owner != 2:
        raise Exception("Erreur, on attendait un X dans la grille 1,2 et la case 2,2")
        
    if player.win_grid(grid_position = (1,2),player=player) :                                  #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (1,2)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")                        
    
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position()) 
    
    print("\n13eme coup :Le premier joueur joue")                
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 1:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 1")
    if not (2,2) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 2,2")	
        
    player.play(grid_position=(2,2), case_position = (3,1))  #le joueur joue
    if board.get_case(grid_position=(2,2), case_position=(3,1)).owner != 1:
        raise Exception("Erreur, on attendait le joueur 1 dans la grille 2,2 et case 3,1")
    
    if player.win_grid(grid_position = (2,2),player=player) :                                  #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (2,2)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")
        
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position()) 
                
                
    print("\n14eme coup :Le deuxième joueur joue")       
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 2:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 2")
    if not (3,1) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 3,1")	
        
    player.play(grid_position=(3,1), case_position = (2,2))  #le joueur joue
    if board.get_case(grid_position=(3,1), case_position=(2,2)).owner != 2:
        raise Exception("Erreur, on attendait un X dans la grille 3,1 et la case 2,2")
        
    if player.win_grid(grid_position = (3,1),player=player) :                                  #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (3,1)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")                        
    
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position()) 
                
    print("\n15eme coup :Le premier joueur joue")                
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 1:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 1")
    if not (2,2) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 2,2")	
        
    player.play(grid_position=(2,2), case_position = (1,3))  #le joueur joue
    if board.get_case(grid_position=(2,2), case_position=(1,3)).owner != 1:
        raise Exception("Erreur, on attendait le joueur 1 dans la grille 2,2 et case 1,3")
    
    if player.win_grid(grid_position = (2,2),player=player) :                                  #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (2,2)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")
        
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position()) 
                
                
    print("\n16eme coup :Le deuxième joueur joue")       
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 2:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 2")
    if not (1,3) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 1,3")	
        
    player.play(grid_position=(1,3), case_position = (2,2))  #le joueur joue
    if board.get_case(grid_position=(1,3), case_position=(2,2)).owner != 2:
        raise Exception("Erreur, on attendait un X dans la grille 1,3 et la case 2,2")
        
    if player.win_grid(grid_position = (1,3),player=player) :                                  #la victoire de grid
        raise Exception("on est pas censé avoir gagné la grille")
    if player.win_game(player) :                                             #la victoire totale
        raise Exception("on est pas censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (1,3)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")                        
    
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position()) 
                
    print("\n17eme coup :Le premier joueur joue")                
    player = game.get_current_player() # joueur 2 avant de jouer
    
    if player.symbol != 1:                                     #on vérifie le symbole
        raise Exception("Erreur, on attendait le joueur 1")
    if not (2,2) in player.get_playable_grid():                            #la grille de jeu
        raise Exception("Erreur, on attendait comme grille jouable la grille 2,2")	
        
    player.play(grid_position=(2,2), case_position = (2,2))  #le joueur joue
    if board.get_case(grid_position=(2,2), case_position=(2,2)).owner != 1:
        raise Exception("Erreur, on attendait le joueur 1 dans la grille 2,2 et case 2,2")
    
    if not player.win_grid(grid_position = (2,2),player=player) :                                  #la victoire de grid
        raise Exception("on est  censé avoir gagné la grille")
    if not player.win_game(player) :                                             #la victoire totale
        raise Exception("on est censé avoir gagné la partie")        
    if player.draw_grid(grid_position = (2,2)) : 
        raise Exception("on est pas censé avoir égalité dans la grille")                         #l'égalité sur great grid      
    if player.draw_game() :                                              #égalité totale
        raise Exception("on est pas censé avoir égalité dans la partie")
        
    for i in range (9) :
        grid=board.grids[i]
        for j in range(9):
            case=grid.cases[j]
            if case.case_is_full():
                print(grid.get_grid_position(),case.get_case_position())