import pygame
import sys
from src.Dinosaur import Dinosaur
from src.obstacle import Obstacle
from src.Button import Button
from src.Scroll import ScrollingBackground

class Controller:
  def __init__(self):
    #setup pygame data
    pygame.init()
    size = width,height = 1280, 720
    self.screen=pygame.display.set_mode(size)
    pygame.display.set_caption("Dinosaur Game!")
    self.state="menu"
    self.clock = pygame.time.Clock()
    BG = pygame.image.load("assets/dinobg.jpg")
    BG = pygame.transform.scale(BG,(1280,720))
    self.screen.blit(BG,(0,0))
    pygame.display.flip()

  def mainloop(self):
    while True:
       if self.state=="menu":
          self.menuloop()
       elif self.state=="game":
          self.gameloop()
    
  def menuloop(self):
     while self.state=="menu":
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        PLAY_BUTTON = Button(image=pygame.image.load("assets/basicButton.png"), pos=(640, 250),
                           text_input="PLAY", font=self.get_font(75), base_color="white", hovering_color="plum")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/basicButton.png"), pos=(640, 400),
                           text_input="OPTIONS", font=self.get_font(75), base_color="white", hovering_color="plum")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/basicButton.png"), pos=(640, 550),
                           text_input="QUIT", font=self.get_font(75), base_color="white", hovering_color="plum")
        self.screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
           button.changeColor(MENU_MOUSE_POS)
           button.update(self.screen)
      
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    scrolling_bg = ScrollingBackground(1280, 720, "assets/dinobg.jpg")
                    scrolling_bg.run()
               if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                   self.options()
               if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                   pygame.quit()
                   sys.exit()
        pygame.display.update()
  def get_font(self,size):
   return pygame.font.Font(None,size)
  def gameloop(self):
    dinosaur=Dinosaur(60)
    lastFrame=pygame.time.get_ticks()
    while True: #gameLoop it draws the frames of the game 
       t = pygame.time.get_ticks() #Get current time
       deltaTime = (t-lastFrame)/1000.0 #Find difference in time and then convert it to seconds
       lastFrame = t #set lastFrame as the current time for next frame.

       for event in pygame.event.get(): #Check for events
        if event.type == pygame.QUIT:
            pygame.quit() #quits
            quit()
        if event.type == pygame.KEYDOWN: #If user uses the keyboard
            if event.key == pygame.K_SPACE: #If that key is space
                dinosaur.jump() #Make dinosaur jump
        dinosaur.update(deltaTime)
        dinosaur.draw(self.screen)

  def options(self):
     while True:
       OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

       self.screen.fill("white")

       OPTIONS_TEXT =self.get_font(45).render("This is the OPTIONS screen.", True, "Black")
       OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
       self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
      
       OPTIONS_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

       OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
       OPTIONS_BACK.update(self.screen)

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                   self.mainloop()
       pygame.display.update()
    
  def gameoverloop(self):
    pass
     #event loop


     #update data


     #redraw



