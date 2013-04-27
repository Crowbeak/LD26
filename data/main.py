import pyglet

import resources
import potato
import needle

game_window = pyglet.window.Window(800, 600)
game_window.set_caption("Poke")
game_window.set_mouse_visible(False)

bg = pyglet.sprite.Sprite(img=resources.bg_img)
potato = potato.Potato()
needle = needle.Needle(potato)

"""
cursor = pyglet.window.ImageMouseCursor(resources.needle_img,
                                        resources.needle_img.width,
                                        resources.needle_img.height)
game_window.set_mouse_cursor(cursor)
game_window.set_mouse_visible(True)
"""

@game_window.event
def on_draw():
    game_window.clear()
    bg.draw()
    potato.draw()
    for eye in potato.eyes:
        eye.draw()
    needle.draw()

def update(dt):
    if potato.opacity < 255:
        potato.opacity += 5
        for eye in potato.eyes:
            eye.opacity += 5
    elif potato.is_dead:
        resources.oh.play()
        potato.reinitialize()

game_window.push_handlers(needle)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
