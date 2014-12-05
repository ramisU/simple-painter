"""
This class simulates a pen that of course can draw on a PyGame surface
"""

from colors import *
import pygame

class Pen:
    """This function only works if pygame.init() was called."""

    def __init__(self, surface, color=BLACK, radius=5, drawwidth=0):
        self.surface = surface
        self.color = color
        self.drawwidth = drawwidth
        self.radius = radius
        self.center = (0, 0)
        self.circ = pygame.draw.circle(self.surface, WHITE, self.center, self.radius, self.drawwidth)
        pygame.display.update()
    #
    
    def draw(self, pos):
        self.center = pos
        self.circ = pygame.draw.circle(self.surface, self.color, self.center, self.radius, self.drawwidth)
        pygame.display.update()
    #

    def set_color(self, new_color):
        self.color = new_color
        self.circ = pygame.draw.circle(self.surface, self.color, self.center, self.radius, self.drawwidth)        
        pygame.display.update()
    #
#

# Not used yet
class Rubber:
    """This function only works if pygame.init() was called."""

    def __init__(self, surface, color=WHITE, rubber_size=(10, 10)):
        self.surface = surface
        self.color = color
        self.size = rubber_size
        self.width = self.size[0]
        self.height = self.size[1]
        self.rubber_rect = pygame.draw.rect(self.surface, self.color, pygame.rect.Rect(0, 0, self.width, self.height))
        pygame.display.update()
    #
    
    def clear(self, pos):
        self.rubber_rect = pygame.draw.rect(self.surface, self.color, [pos, (self.width, self.height)])
        pygame.display.update()
    #
#
