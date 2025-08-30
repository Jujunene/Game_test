#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WINDOW_HEIGHT, WINDOW_WIDTH
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'bg_lvl1':
                return Background('bg_lvl1', (0,0))

            case 'char_1':
                return Player('char_1', ((WINDOW_WIDTH/2), (WINDOW_HEIGHT/2 + 100)))




        return None






        
