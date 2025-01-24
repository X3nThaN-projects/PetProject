import pygame
class Settings:
    def __init__(self, width = 320, heght = 240, font = None):
        self._WND_SIZE = (width, heght)
        self._menu_font = font

    def getWND_SIZE(self):
        return self._WND_SIZE
    
    def get_menu_font(self)->pygame.font.Font:
        return self._menu_font