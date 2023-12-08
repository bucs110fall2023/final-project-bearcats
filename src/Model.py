import pygame
class Start():
    def __init__(self,x,y,image_file="assets/spacetostart.png"):
        self.x=x
        self.y=y
        self.image=pygame.image.load(image_file)
        self.rect=self.image.get_rect()      
class Dinosaur:
    def __init__(self,image_file="assets/run.png"):
        super().__init__() 
        self.image = pygame.image.load(image_file)
        self.x=80
        self.y=500
        self.step_index = 0
        self.jump_vel = 10
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x
        self.dino_rect.y = self.y
        self.dino_jump=False

    def jump(self,x,y):
        self.dino_jump=True
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 1
        if self.jump_vel < - self.jump_vel:
            self.dino_jump = False
            self.jump_vel = self.jump_vel
    def draw(self,screen,image):
        screen.fill("white")
        screen.blit(image,(self.dino_rect.x,self.dino_rect.y))
        pygame.display.flip()
        

class Obstacle():
    def __init__(self, x,y,image_file="assets/cactus.png"):
        # Load the obstacle image
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()

        # Initial position
        self.rect.x = x
        self.rect.y = 300

    def update(self):
        # Update the obstacle's position (e.g., move to the left)
        self.rect.x -= 5
