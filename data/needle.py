import pyglet

import resources
from util import distance

class Needle(pyglet.sprite.Sprite):
    def __init__(self, potato, score, *args, **kwargs):
        super(Needle, self).__init__(img=resources.needle_img, *args, **kwargs)
        
        self.scale = 0.3
        self._potato = potato
        self._score = score
    
    def on_mouse_press(self, x, y, button, modifiers):
        for eye in self._potato.eyes:
            if distance((x, y), (eye.x, eye.y)) < 30 and self._score.time > 0:
                eye.kill()
                self._score.eyes_poked += 1
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.x, self.y = x, y