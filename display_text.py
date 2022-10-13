import pygame


class DisplayText():
    def __init__(self, x, y, color, text, text_size):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.text_size = text_size
        self.text_font = pygame.font.Font("square_font.ttf", text_size)

    def DrawText(self, screen):
        text_tbd = self.text_font.render(self.text, True, self.color)
        screen.blit(text_tbd, (self.x, self.y))
    
    def SetText(self, text):
        self.text = text