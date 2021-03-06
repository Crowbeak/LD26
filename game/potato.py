#TODO: Prevent overlapping eyes.

import random
import pyglet

import resources
from util import distance

random.seed()

class _Eye(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(_Eye, self).__init__(img=resources.eye_img, *args, **kwargs)
        
        self.scale = 0.1
        self.x = 400 + random.randint(-200, 200)
        self.y = 300 + random.randint(-200, 200)
        self.opacity = 0
        
        rotation = random.randint(350, 370)
        if rotation > 360:
            rotation -= 360
        self.rotation = rotation
        
        self.dead = False
    
    def kill(self):
        if not self.dead:
            self.dead = True
            self.image = resources.eye_closed_img
            resources.ow.play()

class Potato(pyglet.sprite.Sprite):
    '''
    Creates an instance of a Doom Potato.
    '''
    def __init__(self, *args, **kwargs):
        super(Potato, self).__init__(img=resources.potato_img, *args, **kwargs)
        
        self.x, self.y = 400, 300
        self.rotation = random.randint(0, 360)
        self.opacity = 0
        
        self.eyes = []
        for i in range(random.randint(2,6)):
            new_eye = _Eye()
            while distance((new_eye.x, new_eye.y)) > 200:
                new_eye = _Eye()
            self.eyes.append(new_eye)
    
    def reinitialize(self):
        self.__init__()