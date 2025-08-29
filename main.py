from operator import truediv

import pygame

print('Setup Start')
pygame.init()  # preparing pygame
#window size definition
window = pygame.display.set_mode((700, 580), ) #pygame.FULLSCREEN
print('Setup End')

while True:
    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  #close window
            exit()    #end pygame
        #fullscreen event (ESC to exit)
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_ESCAPE:
        #         exit()

