#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image


class Entity (ABC):
    def __init__(self, name:str, position:tuple):
        self.name = name
        self.surf = pygame.image.load( './asset/' + name + '.png') # carregando a imagem do personagem pelo nome
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # definindo o rectangulo
        self.speed = 0

    @abstractmethod #decorador que indica que o metodo é abstrato
    def move(self, ):
        pass
