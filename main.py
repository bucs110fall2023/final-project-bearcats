import pygame
#import your controller
from src.controller import Controller
def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    game_controller = Controller()
    game_controller.mainloop()
   
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######


# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()


