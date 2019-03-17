# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:06:03 2019

@author: pierr
"""

ended=False             #identifie si la partie est finie
turn = "joueur 1"             #indique quel joueur joue
move_number=0            #indique le nombre de coup


class MiniGrid:
    def __init__(self, X,Y) :
        self.X=X
        self.Y=Y
        self.on=False          #indique si la mini-grille est terminée (win_situation ou draw_situation)

class Square:                    #objet qui reçoit les ronds ou les croix
    def __init__(self, X, Y, x ,y):
        self.X=MiniGrid.X                #position X  (abscisse de la mini-grille dans la grille)
        self.Y=MiniGrid.Y                #position Y  (ordonnée de la mini-grille dans la grille)
        self.x=x                #position x  (abscisse de la case dans la mini-grille)
        self.y=y                #position y  (ordonnée de la case dans la mini-grille)
        self.on=False           #est-ce que la case est activée ?  True = oui et False = non
        self.player=0           #permettra de savoir par quel joueur la case est activée
            
    def Select(self):                       #quand la souris clique
            if not MiniGrid.on  and not self.on and not ended:   #si la mini-grille n'est pas terminée, que la case est vide (inactive) et que le jeu n'est pas fini
                move_number +=1              #un coup en plus
                self.on=True                #on active la case
                if turn == "joueur 1" :     #si c'est le tour de j1 on trace son symbole
                    self.player=1
                    self.drawObject1()    #les fonctions traceObjet1 et traceObjet2 seront définies dans la partie graphique du code
                    turn="joueur 2"             #c'est au tour de l'autre joueur
                else :
                    self.player=2
                    self.darwObject2() 
                    turn="joueur1"
                    
            if win_situation != 0 :         #on teste s'il y a une situation de victoire
                ended = True                #si oui, la partie est finie et on indique le vainqueur
                if win_situation == 1 :
                    print (player1.surname,"a gagné la partie !")
                else :
                    print (player2.surname,"a gagné la partie !")


class Grid:                     #On crée la grille
    HEIGHT=9                      #les dimensions
    WIDTH=9
    
    def __init__(self):
        for k in range (1,4) :
            for l in range (1,4):
                for i in range (1,(HEIGHT/3)+1) :
                    for j in range (1,(WIDTH/3)+1) :
                      i,j=Square.__init__(k,l,i,j)

class Player:                       #on crée nos 2 joueurs   
    def __init__(self, surname):
        self.surname=surname




def where_to_play(x,y):         #recoit les coordonnes x y du dernier pion placé
    X=x
    Y=y 
    if win_mini_grid ==  1 :
        return 0
    return(X,Y) #renvoie le couple (X,Y) place de la mini grille dans laquelle le jeu se poursuivra

#les fonctions suivantes : "win_ligne","win_colonne","win_diagonale" sont utilise pour voire si un joueur utilisant le pion represnete par
#un objet a gagne dans une  mini grille. Ils seront utilisé dans "win_mini_grille".
def win_line(objet,num_ligne): #determine si un joueur a gagne dans une mini grille suivant une ligne, objet designe X ou O
    x=1
    if (objet(x,num_ligne)==objet(x+1,num_ligne)) and (objet(x,num_ligne)==objet(x+2,num_ligne)): 
        return True
    else:
        return False
    
def win_column (objet,num_colonne): #determine si un joueur a gagne dans une mini grille suivant une colonne
    y=1
    if (objet(num_colonne,y)==objet(num_colonne,y+1)) and (objet(num_colonne,y)==objet(num_colonne,y+2)): 
        return True    
    else:
        return False

def win_diagonal(objet):  #determine si un joueur a gagne dans une mini grille suivant la diagonale 
    y=1
    x=1
    if (objet(x,y)==objet(x+1,y+1)) and (objet(x,y)==objet(x+2,y+2)):
        return True
    else:
        return False

def win_mini_grid(objet,X,Y):         #determine si un joueur a gagne dans une mini grille en rassemblant toutes les cas   
    for i in range (1,4):             #i parcours les lignes et colonnes
        if (win_line(objet,i)) or (win_diagonal(objet)) or (win_column(objet,i)):
            return True
    return False




# les fonctions win_LIGNE, win_COLONNE, win_DIAGONALE determine si un joueur a gagne suivant la ligne consititue de 3 mini grilles etc..    
def win_LINE(objet):
    for Y in range (1,4): #determine si un joueur a gagne suivant une lIGNE
        a=0
        for X in range (1,4):
            if win_mini_grid(objet,X,Y):
                a+=1
            if a==3 :
                return True  

def win_COLUMN(objet):
    for X in range (1,4): #determine si un joueur a gagne suivant une colonne
        a=0
        for Y in range (1,4):
            if win_mini_grid(objet,X,Y):
                a+=1
            if a==3 :
                return True
        else :
            return False

def win_DIAGONAL(objet) :
    X=1                 #determine si un joueur a gane suivant la diagonale
    Y=1
    a=0
    for i in range (0,3):
        if win_mini_grid(X+i,Y+i):
            a+=1
        if a==3:
            return True
        else:
            return False
    
def win_situation(objet1,objet2):           # prends en parametre les deux objets chosit par les deux joueurs et detemine si l'un des deux a gagne         
        if win_COLUMN(objet1) or win_DIAGONAL(objet1) or win_LINE(objet1):
            return 1
        if win_COLUMN (objet2) or win_DIAGONAL(objet2) or win_LINE(objet2):
            return 2
        return False    
    
def draw_situation (X,Y) : 
    if win_mini_grid(objet1,X,Y)   and win_mini_grid(objet2,X,Y) and Square.on == True :
        return True
    return False


#---------------------------------------------------------------------------------------------------
        
