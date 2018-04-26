
# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
pygame.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('SpongeBob.mp3')#https://www.youtube.com/watch?v=vE2ETqUGj6Q
pygame.mixer.music.play(-1)
BackGround = pygame.image.load('KRUSTY_KRAB.jpg')#https://twitter.com/krustykrabtw

# Define some colours

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
BLUE = (0,0,200)
BRIGHT_BLUE=(0,0,255)
Blue1= (75, 198, 185)
Blue2 = (115, 193, 198)
Blue3 = (135, 241, 255)
Blue4= (150, 195, 206)
Blue5=(67, 188, 205)

SCREENWIDTH = 400
SCREENHEIGHT = 400
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

class Button():
    """This is a class for a generic button.
    
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(100, 40), font_name="centurygothic", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GRAY  # mouseover color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()
sound = False
def my_shell_function():
    """A generic function that prints something in the shell"""
    print('Fire the nukes!')

def my_next_function():
    """A function that advances to the next level"""
    global level
    level +=1

def my_settings_function():
    """A function that advances to the next level"""
    global level
    level +=1

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    level -= 1

def my_soundsOn_function():
    print('Sounds On')

def my_soundsOff_function():
    print('Sounds Off')
        
def my_hello_function():
    print('Spongebob says "KRABBY PATTIES NEED LOVE TOO!"')

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in level2_buttons:

            if button.rect.collidepoint(pos):
                button.call_back()

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects
button_01 = Button("FLIP NOW!", (SCREENWIDTH/2, SCREENHEIGHT/4), my_hello_function,bg=Blue3)
button_Settings = Button("Settings", (SCREENWIDTH/2, SCREENHEIGHT/2), my_settings_function,bg=(20,200,35))
button_02 = Button("Back", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_previous_function)
button_03 = Button("Quit", (SCREENWIDTH/2, SCREENHEIGHT*6/7), my_quit_function, bg=(200,25,35))
button_SoundsOn = Button("On", (150, SCREENHEIGHT/2), my_soundsOn_function,bg=(20,200,35))
button_SoundsOff = Button("Off", (250, SCREENHEIGHT/2), my_soundsOff_function,bg=(200,25,35))


#arrange button groups depending on level
level1_buttons = [button_01, button_03, button_Settings]
level2_buttons = [button_02, button_SoundsOn, button_SoundsOff]

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)

    # --- Game logic goes here

    # --- Draw code goes here

    # Clear the screen to white
    screen.blit(BackGround,(0, 0))

    # Draw buttons
    if level == 1:
        for button in level1_buttons:
            button.draw()
        font = pygame.font.SysFont('centurygothic', 26)
        text = font.render("EXTREME KRABBY PATTY FLIP", 1, (BLACK))
        screen.blit(text, (35, 10))
    elif level == 2:
        #Settings Title
        font = pygame.font.SysFont('centurygothic', 36)
        text = font.render("Settings", 1, (BLACK))
        screen.blit(text, (150, 1))
        #Sound Subtitle
        font = pygame.font.SysFont('centurygothic', 24)
        text = font.render("Sound", 1, (BLACK))
        screen.blit(text, (170, 50))
        for button in level2_buttons:
            button.draw()

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

