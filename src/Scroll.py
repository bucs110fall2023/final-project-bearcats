import pygame
import sys
import math
import random

class ScrollingBackground:
    def __init__(self, width, height, image_path):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((width, height))
        self.bg = pygame.image.load(image_path)
        self.bg = pygame.transform.scale(self.bg, (width, height))
        self.scroll = 0
        self.tiles = math.ceil(width / self.bg.get_width()) + 1

    def wait_for_space(self):
        waiting = True
        self.screen.blit(self.bg,(0,0))
        self.screen.blit(pygame.image.load("assets/dinoJump.png"),(80,490))
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
            i = 0
            while i < self.tiles:
                self.screen.blit(self.bg, (self.bg.get_width() * i + self.scroll, 0))
                i += 1
            self.scroll -= 6
            if abs(self.scroll) > self.bg.get_width():
                self.scroll = 0
            self.dinoJump()
            pygame.display.update()
    def dinoJump(self):
        self.rect = pygame.image.load("assets/dinoJump.png").get_rect()
        self.rect.x=80
        self.rect.y=490
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.rect.y-=20
                        self.draw
                    
    def draw(self):
        self.image = pygame.image.load("assets/dinoJump.png")
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.display.flip()
