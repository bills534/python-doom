from sprite_object import *


class ObjectHandler:
    def __init__(self, game) -> None:
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite

        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game)) # these first two load the predefined sprites from the sprite object class
        add_sprite(AnimatedSprite(game, pos=(10.75, 7.75)))
        add_sprite(AnimatedSprite(game, pos=(12.25, 7.75)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(7.75, 1.25)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.25, 1.25)))

    

    def update(self):
        [sprite.update() for sprite in self.sprite_list]


    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)