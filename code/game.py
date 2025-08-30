#!/usr/bin/python
# -*- coding: utf-8 -*-
#importando classes e bibliotecas necessarias
import pygame

from code.const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self): #o construtor da classe vai inicializar o pygame e criar a janela do jogo
        pygame.init()  # preparing pygame
        # window size definition
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), )  # pygame.FULLSCREEN


    def run(self, ):
          while True:
            menu = Menu(self.window)    #passando a janela como parametro
            menu_return = menu.run()      # para aparecer o menu na tela

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:   #vai passar o nivel 1 e depois o level 2
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()


            elif menu_return == MENU_OPTION[3]:
                pass
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                exit()
            else:
                pass
