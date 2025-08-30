#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.entity import Entity


class Level:
    def __init__(self, window, name, game_level):
        self.window = window
        self.name = name
        self.game_level = game_level # Reference to the main game level object
        self.entity_list: list[Entity] = []

    def run(self, ):
        pass
