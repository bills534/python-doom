import pygame as pg

_ = False  # this makes the following map more 'readable'
mini_map = [
    #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
    [_, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, _],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 1, 1, 1, 1, 1, _, _, _, 2, _, _, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, 1],
    [1, 1, 1, 3, 3, 1, 1, 1, _, 1, 1, _, 1, 1, 1, 1],
    [3, _, _, _, _, _, _, _, 3, _, _, _, _, _, _, 4],
    [3, _, _, _, _, _, _, _, 3, _, _, _, _, _, _, 4],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [3, _, _, _, _, _, _, _, 3, _, _, _, _, _, _, 4],
    [1, 3, 3, 3, 3, 3, 3, 3, _, 4, 4, 4, 4, 4, 4, 1],
]

class Map:
    def __init__(self, game) -> None:
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
    
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:  # if minimap array is not blank, generate an x.y coordinate and put into world map array
                    self.world_map[(i,j)] = value
    
    def draw(self):
        [
            pg.draw.rect(self.game.screen, 'darkgrey', (pos[0]*100, pos[1]*100, 100, 100), 2)
            for pos in self.world_map
        ]