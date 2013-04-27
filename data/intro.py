import pyglet

import resources

class Title(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Title, self).__init__(img=resources.crow_logo, x=760, y=40,
                                    *args, **kwargs)
        self.game_title = pyglet.text.Label("Poke", font_size = 36,
                                            x=40, y=500, color=(0,0,0,255))
        self.credits = pyglet.text.Label("A game by Lena LeRay",
                                         x=40, y=450, color=(0,0,0,255))
        self.timer = 200