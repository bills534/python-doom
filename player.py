from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        # WASD controls
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        # apply calculated movement
        self.check_wall_collision(dx, dy)

        # rotation
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        
        self.angle %= math.tau  # tau is 2*pi, I have no idea why this is here

    
    def check_wall(self, x, y):
        # if the player position is not listed in the world map then it is valid
        # world map is effectivly a map of restricted areas
        return (x, y) not in self.game.map.world_map
    

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        pg.draw.line(
            self.game.screen,  # surface
            'yellow',  # color
            (self.x * 100, self.y * 100),  # start position
            (self.x * 100 + WIDTH * math.cos(self.angle), self.y * 100 + WIDTH * math.sin(self.angle)),  # end position
            2  # width
        )
        pg.draw.circle(
            self.game.screen,  # surface
            'green',  # color
            (self.x * 100, self.y * 100),  # position
            15  # radius
        )

    def update(self):
        self.movement()
    
    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)