import pygame  
import copy

pygame.init()

from addition import IsWin
from time import *

from IA.IA_Full_Random import *
from IA.IA_Full_Left import *
from IA.IA_Proba_V1 import *
from IA.IA_Proba_V2 import *

from display_text import *

class Game():
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width

        self.game_screen = "play_scene"

        self.main_clock = pygame.time.Clock()
        self.counter = 0

        self.player = ["ordi", "ordi"]
        self.ordi = [IAProbaV2(), IAProbaV1()]

        self.user_win = [0, 0]

        self.numbers_games = 10

        self.win_text_red = DisplayText(20, 600, (255, 255, 255), "win: Red", 80)
        self.win_text_blue = DisplayText(20, 600, (255, 255, 255), "win: Blue", 80)
        self.win_text_tie = DisplayText(20, 600, (255, 255, 255), "win: Tie", 80)

        self.start_turn = 1

        self.InitSimu()

    def InitSimu(self):
        self.playing = True
        self.winner = None
        self.running = True
        self.grid = self.SetGrid()
        self.turn = self.start_turn
        self.go_next_game = False

        if self.start_turn == 1:
            self.start_turn = 2
        else:
            self.start_turn = 1
        
        self.wait_click = False

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
                        #equalité
                        pass
                    elif not self.wait_click:
                        #execute if win
                        self.user_win[self.winner - 1] += 1
                    if self.player[0] == "user" or self.player[1] == "user":
                        self.wait_click = True
                    else:
                        self.InitSimu()
                        break
                #check if user play
                if self.go_next_game:
                    self.InitSimu()
                    break
        for i in range(2):
            print(self.user_win[i], self.ordi[i].GetName())
    
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
            if self.game_screen == "play_scene":
                #check for 1 input key
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        #left button
                        if self.who_play == "user" and self.wait_click == False and self.playing == True:
                            self.mouse_pressed = True
                            mouse_pos = pygame.mouse.get_pos()
                            self.AddToken(mouse_pos[0]//100, self.turn)
                        elif self.wait_click == True:
                            self.go_next_game = True

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

            #print circles
            self.Draw(self.grid)
        
            #play_ordi
            if self.who_play == "ordi" and self.playing:
                grid_copy = copy.deepcopy(self.grid)
                pygame.display.flip()

                self.AddToken(self.ordi[self.turn - 1].Calc(grid_copy, self.turn), self.turn)
            if self.wait_click:
                if self.winner == 0:
                    self.win_text_tie.DrawText(self.screen)
                elif self.winner == 1:
                    self.win_text_red.DrawText(self.screen)
                elif self.winner == 2:
                    self.win_text_blue.DrawText(self.screen)

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
screen_height = 700

#set la fenetre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puissance 4")

#cree le jeu a partir le l'objet 'game'
game1 = Game(screen, screen_width, screen_height)

#lance la boucle global

result = game1.Run()

#quitte pygame
pygame.quit()