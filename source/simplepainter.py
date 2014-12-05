"""
AUTHOR: Nelson Dos Santos
CREATED: 5.12.2014
TOPICS: PyGame, events, event handling, self.text, labels, menus, colors, quiting pygame.display
DESCRIPTION: Simple painter class which allows you to draw.
"""

from tools import *  # Pen, Rubber and pygame
from colors import *
from menu import Menu


class SimplePainter:
    """This class uses PyGame to draw on the screen.
This class does not call 'pygame.init()', you have to do it!
"""

    # static variable
    rules = ["This program allows you to draw and erase what you draw.", " ", " ", "Type the letter corresponding to the action:", " ", " ",
             "Pencil: P", " ", "Rubber: C", " ", "Clear screen: N", " ",
             "Red pencil: R", " ", "Blue pencil: B", " ", "Green pencil: G", " ", "Black pencil: P", " ", "Start/stop music: M"]

    name = 'Simple Painter'

        
    # shows menu
    def menu(self):
        # Creating an object of type Menu
        menu = Menu(SimplePainter.name, (640, 480), BLACK, WHITE,
                    (100, 400), (480, 400), SimplePainter.rules)              


    # constructor
    def __init__(self, resolution, bg=WHITE, pen_color=BLACK, pen_size=2):
        """This method __init__ does not check the type of the variables. In general, for this application,
no type checking has been made for performance reasons. Be sure
"""
        
        self.menu() # needs firts 'pygame.init()' to be called!
        
        self.resolution = resolution
        self.screen = pygame.display.set_mode(self.resolution)
        self.bg = bg        
        self.screen.fill(self.bg)
        self.pen_color = pen_color
        self.pen_size = pen_size
        self.pen = Pen(self.screen, self.pen_color, self.pen_size)
        
        self.is_drawing = False
        self.clock = pygame.time.Clock()
        self.FPS = 300

        # You can add more music here and create a playlist!
        self.music = [pygame.mixer.Sound('sounds/beat_1.wav')]
          
        self.font_size = 20
        self.font = pygame.font.Font(None, self.font_size)
        self.tool = 'Tool: '
        self.tools = ['Pencil', 'Rubber']
        self.tool_pos = (10, 10)
        self.text = self.font.render(self.tool + self.tools[0], True, RED)
        self.write(self.tool + self.tools[0], self.tool_pos)
        
        pygame.mixer.music.load('sounds/pen.wav')
        pygame.display.set_caption('Simple Painter')
        pygame.display.update()
    #

    def clear(self, pos, width, height):
        rubber = pygame.draw.rect(self.screen, self.bg, pygame.rect.Rect(pos, (width, height)))
        pygame.display.update()
    #
    
    def write(self, msg, pos, color=RED):
        self.text = self.font.render(msg, True, RED)
        """ This function updates the display calling pygame.display.update()"""        
        self.screen.blit(self.text, pos)
        pygame.display.update()
    #
    
    def start(self):
        """This function is called when you enter in drawing mode."""
        self.is_drawing = True
        
        pen_down = False
        save = False
        color_changed = False
        playing = False
        
        while self.is_drawing:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    if pen_down:
                        self.pen.draw(pygame.mouse.get_pos())
                        pygame.mixer.music.play()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pen_down = True
                                
                if event.type == pygame.MOUSEBUTTONUP:
                    pygame.mixer.music.stop()                    
                    pen_down = False

                # enables pen or rubber, or clears the screen
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        pen_down = True
                        self.pen.set_color(self.pen_color)
                        pygame.mixer.music.stop()
                        self.screen.fill(self.bg)                
                        self.write(self.tool+self.tools[0], self.tool_pos)

                    elif event.key == pygame.K_c:
                        self.pen.set_color(self.bg)
                        self.clear(self.tool_pos, 100, 40)
                        self.write(self.tool+self.tools[1], self.tool_pos)
                        
                    elif event.key == pygame.K_p:
                        self.pen.set_color(self.pen_color)
                        self.clear(self.tool_pos, 100, 40)
                        self.write(self.tool+self.tools[0], self.tool_pos)
                        
                    elif event.key == pygame.K_m:
                        if playing:
                            playing = False
                        else:
                            playing = True
                            
                        if not playing:
                            self.music[0].play()
                        else:
                            self.music[0].stop()
                            
                    # setting colors
                    elif event.key == pygame.K_b:
                        self.pen.set_color(BLUE)
                    elif event.key == pygame.K_r:
                        self.pen.set_color(RED)
                    elif event.key == pygame.K_g:
                        self.pen.set_color(GREEN)
                
                if event.type == pygame.QUIT:
                    self.is_drawing = False

            self.clock.tick(self.FPS)
            pygame.display.update()

    # END start
    
# END class
