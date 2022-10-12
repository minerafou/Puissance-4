import pygame  

pygame.init()

from addition import IsWin
from time import *

from IA.IA_Full_Random import *
from IA.IA_Full_Left import *


class Game():
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width

        self.game_screen = "play_scene"

        self.main_clock = pygame.time.Clock()
        self.counter = 0

        self.player = ["user", "user"]
        self.ordi = [IAFullLeft(), IAFullRandom()]

        self.user_win = [0, 0]

        self.numbers_games = 100

        self.InitSimu()

    def InitSimu(self):
        self.playing = 1
        self.winner = None
        self.running = True
        self.grid = self.SetGrid()
        self.turn = 1

    def SetGrid(self):
        grid = []
        for i in range(7):
            grid.append([])
            for j in range(6):
                grid[i].append(0)
        return grid

    def Run(self):
        for i in range(self.numbers_games):
            while self.running:
                self.HandleEvent()
                self.Update()
                self.Refresh()
                self.main_clock.tick(60)
                if self.winner != None:
                    if self.winner == 0:
                        pass
                    else:
                        self.user_win[self.winner - 2] += 1
                    self.InitSimu()
                    break
        print(self.user_win)
    
    def HandleEvent(self):

        self.mouse_pressed = False

        #verifie les evenement pygame
        for event in pygame.event.get():
            #check des input joueur
            #input de la croix rouge (en haut a droite de la fenetre)
            if event.type == pygame.QUIT:
                self.running = False

            #check le temps
            if event.type == pygame.USEREVENT:
                self.EveryTenMilliSecAction()
            
            #check input clavier
            if self.game_screen == "play_scene" and self.playing == True:
                #check for 1 input key
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        #left button
                        if self.who_play == "user":
                            self.mouse_pressed = True
                            mouse_pos = pygame.mouse.get_pos()
                            self.AddToken(mouse_pos[0]//100, self.turn)

                    elif event.button == 3:
                        #right button
                        pass
                    
                    elif event.button == 2:
                        #middle button
                        pass

    def Update(self):
        #update screen size
        self.screen_width, self.screen_height = self.screen.get_size()

        #delete tous sur l'ecran
        self.screen.fill((0, 0, 0))

        if self.game_screen == "play_scene":
            temp_winner = IsWin(self.grid)
            if temp_winner != None and self.playing:
                self.Win(temp_winner)
        
            #check who play
            self.who_play = self.player[self.turn - 1]
        
            #play_ordi
            if self.who_play == "ordi" and self.playing:
                self.AddToken(self.ordi[self.turn - 1].Calc(self.grid), self.turn)
            
            #print circles
            self.Draw(self.grid)

            #check for full
            temp_count_full = 0
            for i in range(7):
                if self.grid[i][5] != 0:
                    temp_count_full += 1
            if temp_count_full == 7:
                self.Win(0)

    
    def Win(self, user):
        self.playing = False
        self.winner = user

    def AddToken(self, line, color):
        for i in range(6):
            if self.grid[line][i] == 0:
                self.grid[line][i] = color
                if self.turn == 1:
                    self.turn = 2
                else:
                    self.turn = 1
                break

    def Draw(self, grid):
        x = 50
        y = 550
        for i in grid:
            for j in i:
                if j == 0:
                    color = (255, 255, 255)
                if j == 1:
                    color = (255, 0, 0)
                if j == 2:
                    color = (0, 0, 255)
                pygame.draw.circle(self.screen, color, (x, y), 35)
                y -= 100
            x += 100
            y = 550

    def Refresh(self):
        pygame.display.flip()

    def EveryTenMilliSecAction(self):
        self.counter += 1
        if self.counter == 100:
            self.counter = 0

pygame.time.set_timer(pygame.USEREVENT, 10)

screen_width = 700
screen_height = 600

#set la fenetre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puissance 4")

#cree le jeu a partir le l'objet 'game'
game1 = Game(screen, screen_width, screen_height)

#lance la boucle global

result = game1.Run()

#quitte pygame
pygame.quit()