#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name , position)


    def move(self, ):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a]:
            self.rect.centerx -= 1
        pass

