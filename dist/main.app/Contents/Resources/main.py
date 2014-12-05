'''
AUTHOR: Nelson Dos Santos
CREATED: 5.12.2014
Main script for testing 'SimplePainter' class.
'''


import info
info.show()
print(info.__type_errors__)

import pygame
from simplepainter import *

pygame.init()  # DO NOT REMOVE!

resolution = (640, 480)


if __name__ == '__main__': 
    painter = SimplePainter(resolution, WHITE, BLACK)
    painter.start()


# Free all pygame modules after exiting from the main loop
pygame.quit()  # DO NOT REMOVE!
