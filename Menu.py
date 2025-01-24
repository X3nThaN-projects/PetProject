import pygame
import random
from settings import Settings
class Menu:
    def __init__(self, pygame = None, settings = Settings(), screen = pygame.display.get_active(), items = ["1", "2", "3"], background= ""):
        self._pg = pygame
        self._settings = settings
        self._screen = screen
        self._items = items
        self._background_path = background
        self._bckgrnd_x = 0
        self._bckgrnd_y = 0
        self._point = 0

    def render_items(self)->bool:
        font = self._settings.get_menu_font()
        order = len(self._items)
        self._screen.blit(self._pg.image.load(self._background_path),
                          (self._bckgrnd_x,           #start x
                          self._bckgrnd_y)            #start y
                        )
        self._bckgrnd_x = self._bckgrnd_x - random.randint(-1, 3)
        self._bckgrnd_y = self._bckgrnd_y - random.randint(-1, 3)
        self._bckgrnd_x = max(self._bckgrnd_x, -250)
        self._bckgrnd_y = max(self._bckgrnd_y, -500)
        for item in self._items:
            text = font.render(item, True, (255, 255, 255))              

            self._screen.blit(text,
                (self._screen.get_width() / 20,
                self._screen.get_height() - 50 * order)
            )
            
            if self._items[self._point] == item:
                self._screen.blit(self._pg.image.load("resources/selected_text.png"),
                          (self._screen.get_width() / 20,           #start x
                          self._screen.get_height() - 50 * order)            #start y
                        )
            

            order = order - 1
        return True
    
    def get_point(self)->int:
        return self._point
    
    def set_point(self, value):
        self._point = max(min(len(self._items) - 1, value), 0)
        print("Current point = ", self._items[self._point])
        return
