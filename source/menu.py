"""
AUTHOR: Nelson Dos Santos
CREATED: 5.12.2014
TOPICS: PyGame, events, event handling, self.text, labels, menus, colors, quiting pygame.display

DESCRIPTION: Simple menu created using PyGame

COMMENT:

If this Menu runs as an independent application, you should call 'pygame.init()'.
You can call it anyway at the beginning of __init__ of Menu  since it's safe:

        http://www.pygame.org/docs/ref/pygame.html#pygame.init
        It is safe to call this init() more than once:
        repeated calls will have no effect.
        This is true even if you have pygame.quit() all the modules

The class does not free any resource being used,
such as the pygame modules, in fact no call to 'pygame.quit()' is executed.
"""

import pygame
from colors import *

'''Note that eveytime you import something,
the code that represents that something is literally copied in the position you are importing it.'''


# Class Menu
class Menu:
    
    def __init__(self, title, resolution, bg, fg, cont_pos, exit_pos, rules):
        """Make sure the type of the variables passed to this __init__ are the following,
(because no type checking is done):
            title := str
            resolution := tuple(int, int)
            bg := tuple(int, int, int) or tuple(int, int, int, int)
            cont_pos := tuple(int, int)
            exit_pos := tuple(int, int)
            tules := list[str, str, ... ]
        """
        
        self.title = title
        self.resolution = resolution
        self.screen = pygame.display.set_mode(self.resolution)
        self.bg = bg
        self.fg = fg
        self.screen.fill(self.bg)
    
        self.cont_pos = cont_pos
        self.exit_pos = exit_pos

        if len(rules) <= 0:
            rules.append('')
        self.rules = rules

        # setting the text of the title
        self.intro_text = pygame.font.Font(None, 60)
        self.intro_lab = self.intro_text.render(self.title, True, self.fg)
        self.intro_rect = self.intro_lab.get_rect()
        self.intro_rect.center = self.screen.get_rect().center
        self.intro_rect = pygame.rect.Rect(self.intro_rect[0], 100,
                                           self.intro_rect[2], self.intro_rect[3])
            
        # setting text for the rules
        self.explan_text = pygame.font.Font(None, 25)

         # setting the 2 buttons for options: exit and continue
        self.text = pygame.font.Font(None, 30)
        
        self.cont_lab = self.text.render('Continue', True, self.fg)
        self.cont_lab_rect = self.cont_lab.get_rect()
        self.cont_lab_rect = pygame.rect.Rect(self.cont_pos[0], self.cont_pos[1],
                                              self.cont_lab_rect[2], self.cont_lab_rect[3])

        self.exit_lab = self.text.render("Exit", True, self.fg)
        self.exit_lab_rect = self.exit_lab.get_rect()
        self.exit_lab_rect = pygame.rect.Rect(self.exit_pos[0], self.exit_pos[1],
                                              self.exit_lab_rect[2], self.exit_lab_rect[3])

        self.proceed = False
        pygame.display.update()
        self.run()
        
    # END __init__
    
    def _quit(self):
        """This function quit the pygame modules and the Python interpreter."""
        pygame.quit()
        quit()

    def show_rules(self):
        """This function shows the rules received in the __init__ function s a list of strings."""
        line_height = 0
        for rule in self.rules:
            explain_lab = self.explan_text.render(rule, True, self.fg)
            explain_rect = explain_lab.get_rect()
            explain_rect.center = self.screen.get_rect().center        
            explain_rect = pygame.rect.Rect(explain_rect[0], 180 + line_height,
                                            explain_rect[2], explain_rect[3])
            self.screen.blit(explain_lab, explain_rect)
            
            line_height += 10
    #
    
    def run(self):
        """This function is called in __init__ to make the whole menu run."""
        while not self.proceed:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self._quit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.cont_lab_rect.collidepoint(pygame.mouse.get_pos()):
                        self.proceed = True
                        
                    if self.exit_lab_rect.collidepoint(pygame.mouse.get_pos()):
                        self._quit()
                    
                if event.type == pygame.MOUSEMOTION:
                    # Checking the mouse over the labels.
                    if self.cont_lab_rect.collidepoint(pygame.mouse.get_pos()):
                        self.cont_lab = self.text.render('CONTINUE', 1, BLUE)
                    else:
                        self.cont_lab = self.text.render('Continue', 1, self.fg)
                        
                    if self.exit_lab_rect.collidepoint(pygame.mouse.get_pos()):
                        self.exit_lab = self.text.render('EXIT', 1, RED)
                    else:
                        self.exit_lab = self.text.render('Exit', 1, self.fg)

            # Restoring the screen
            self.screen.fill(self.bg)

            # Redrawing objects
            self.screen.blit(self.intro_lab, self.intro_rect)
            self.show_rules()
            self.screen.blit(self.cont_lab, self.cont_lab_rect)
            self.screen.blit(self.exit_lab, self.exit_lab_rect)

            # updating the whole display
            pygame.display.flip()
        # END run
    
# END class
