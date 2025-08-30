#!/usr/bin/python
# -*- coding: utf-8 -*-
#importando classes e bibliotecas necessarias
import pygame

from code.const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self): #o construtor da classe vai inicializar o pygame e criar a janela do jogo
        pygame.init()  # preparing pygame
        # window size definition
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), )  # pygame.FULLSCREEN


    def run(self, ):
          while True:
            menu = Menu(self.window)    #passando a janela como parametro
            menu.run()      # para aparecer o menu na tela
            pass
            #check for events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  #close window
            #         exit()    #end pygame
            #     #fullscreen event (ESC to exit)
            #     # if event.type == pygame.KEYDOWN:
            #     #     if event.key == pygame.K_ESCAPE:
            #     #         exit()

