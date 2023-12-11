import pygame
import sys
class Dinosaur():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.x = 50
        self.y = 50
        self.width = 40
        self.height = 60
        self.vel = 5
        self.isJumping=False
        self.jumpCount = 10
        self.clock = pygame.time.Clock()
        self.image=pygame.image.load("assets/dinoJump.png")
    def wait_for_space(self):
        waiting = True
        print(waiting)
        self.screen.blit(self.image,(80,500))
        pygame.display.flip()
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False
    def run(self):
        self.wait_for_space()
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

    
    

