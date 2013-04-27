import pyglet

import resources
from util import distance

class Needle(pyglet.sprite.Sprite):
    def __init__(self, potato, *args, **kwargs):
        super(Needle, self).__init__(img=resources.needle_img, *args, **kwargs)
        
        self.scale = 0.3
        self._potato = potato
    
    def on_mouse_press(self, x, y, button, modifiers):
        for eye in self._potato.eyes:
            if distance((x, y), (eye.x, eye.y)) < 30:
                eye.kill()
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.x, self.y = x, y
    
    def update(self):
        pass