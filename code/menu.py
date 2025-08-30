#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import font, Surface, Rect

from code.const import WINDOW_WIDTH, COLOR_COCOA_BROWN, MENU_OPTION, COLOR_MELON, COLOR_SAGE, COLOR_EARTH_YELLOW, \
    COLOR_IVORY, COLOR_GUNMETAL, COLOR_TURQUOISE, COLOR_RED


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu_bg_a.png')   #fazendo o load da imagem de fundo do menu
        self.rect = self.surf.get_rect(left=0, top=0)      #criando o retangulo do menu

    def run(self, ):
        menu_option = 0   #opção inicial do menu
        #definindo o menu
        pygame.mixer_music.load('./asset/musica_menu.mp3')  # carregando a musica de fundo do menu
        pygame.mixer_music.play(-1)
        while True:  #loop da imagem  do menu
             # a source é a imagem que será desenhada no dest que é a tela do jogo(retangulo criado)
            self.window.blit(source=self.surf, dest=self.rect)   #desenhando a imagem na tela
             #Colocando o texto na tela
            self.menu_text('Nome', COLOR_MELON, ((WINDOW_WIDTH/2), 70), 80 )
            self.menu_text('do Jogo', COLOR_MELON, ((WINDOW_WIDTH / 2), 140), 80)

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(MENU_OPTION[i], COLOR_COCOA_BROWN, ((WINDOW_WIDTH/2), 270 + 60 * i) , 40)

                else:
                    self.menu_text(MENU_OPTION[i], COLOR_IVORY, ((WINDOW_WIDTH/2), 270 + 60 * i) , 40)

                

            # check for events
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()  #close window
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            exit()
                            #end pygame
                #eventos do teclado
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:   #tecla de baixo
                            if menu_option < len(MENU_OPTION) -1:
                                menu_option += 1
                            else:
                                menu_option = 0
                        if event.key == pygame.K_w or event.key == pygame.K_UP:   #tecla de cima
                            if menu_option > 0:
                                menu_option -= 1
                            else:
                                menu_option = len(MENU_OPTION) -1

                        if event.key == pygame.K_RETURN:  #tecla de enter
                            return MENU_OPTION[menu_option]   #retorna a opção selecionada
                #eventos do mouse
                    # if event.type == pygame.MOUSEMOTION:
                    #     if event.pos[0] >= (WINDOW_WIDTH/2 - 100) and event.pos[0] <= (WINDOW_WIDTH/2 + 100):
                    #         for i in range(len(MENU_OPTION)):
                    #             if event.pos[1] >= (270 + 60 * i - 20) and event.pos[1] <= (270 + 60 * i + 20):
                    #                 menu_option = i
                    #
                    #     if event.type == pygame.MOUSEBUTTONDOWN:
                    #         if pygame.mouse.get_pressed((1)):   #botão esquerdo do mouse
                    #             return MENU_OPTION[menu_option]  #retorna a opção selecionada


            pygame.display.flip()   #atualizando a tela

    def menu_text(self, text: str, font_color: tuple, text_pos: tuple, size:int):
        text_font: font.Font = pygame.font.Font('./asset/fonte_pixelart.ttf', size)   #inserindo a fonte do texto
        text_surf: Surface = text_font.render(text, True, font_color)   #criando uma imagem do texto
        text_rect: Rect = text_surf.get_rect(center=text_pos)    #retangulo da imagem(texto)
        self.window.blit(source=text_surf, dest=text_rect)

    def menu_text_2(self, text: str, font_color: tuple, text_pos: tuple, size: int):
        #tentando arredondar o fundo do texto
        text_font: font.Font = pygame.font.Font('./asset/Pixellari.ttf', size)  # inserindo a fonte do texto
        text_surf: Surface = text_font.render(text, True, font_color)  # criando uma imagem do texto
        text_rect: Rect = text_surf.get_rect(center=text_pos)  # retangulo da imagem(texto)
        self.window.blit(source=text_surf, dest=text_rect)
