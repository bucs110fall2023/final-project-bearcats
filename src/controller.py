import pygame
import sys
from src.Model import Start, Dinosaur

class GameController:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.screen=pygame.display.set_mode((1280,720))
        pygame.display.set_caption('Dinosaur Game!!') 
        self.screen.fill("white")
        pygame.display.flip()
        self.state="menu"
        self.is_running=True
        clock =pygame.time.Clock()
        fps=60
        clock.tick(fps)
        # Set up the clock for controlling the frame rate
    def mainloop(self):
        print(self.state)
        while self.is_running:
            if self.state=="menu":
                self.menuloop()
            elif self.state=="game":
                self.gameloop()
            elif self.state=="quit":
                pygame.quit()
    def menuloop(self):
        start=Start(0,360)
        self.screen.blit(start.image,(start.x,start.y))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    print("clicked")
                    self.state="game"
                    self.gameloop()
    def gameloop(self):
        while self.state=="game":
            player=Dinosaur()
            self.screen.fill("white")
            self.screen.blit(player.image,(player.x,player.y))
            self.background()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.state="quit"
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        player.jump(80,50)
            player.draw(self.screen,player.image)
            pygame.display.update()
    def gameoverloop(self):
        pass
    def background(self):
        x_pos_bg=30
        y_pos_bg=550
        bg= pygame.image.load("assets/track.png")
        self.screen.blit(bg, (x_pos_bg, y_pos_bg))
