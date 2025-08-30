#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame import font, Surface, Rect
from code.const import COLOR_IVORY, WINDOW_HEIGHT, COLOR_EARTH_YELLOW
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.menu import Menu


class Level:
    def __init__(self, window, name, game_level):
        self.window = window
        self.name = name
        self.game_level = game_level # Reference to the main game level object
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity('bg_lvl1'))
        self.entity_list.append(EntityFactory.get_entity('char_1')) # adicionando o player na lista de entidades
        self.timeout = 20000  # tempo para completar o level em milisegundos

    def run(self, ):

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)  # FPS
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # desenhando a imagem na tela


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    exit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = Menu(self.window)
                        menu_return = menu.run()

            self.level_text(f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_EARTH_YELLOW,(10, 5), 20)
            self.level_text(f'fps: {clock.get_fps() :.0f} ', COLOR_EARTH_YELLOW, (10, WINDOW_HEIGHT - 35), 14)

            
            pygame.display.flip()

    def level_text(self, text: str, font_color: tuple, text_pos: tuple, size: int):
        #tentando arredondar o fundo do texto
        text_font: font.Font = pygame.font.Font('./asset/Pixellari.ttf', size)  # inserindo a fonte do texto
        text_surf: Surface = text_font.render(text, True, font_color)  # criando uma imagem do texto
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])  # retangulo da imagem(texto)
        self.window.blit(source=text_surf, dest=text_rect)