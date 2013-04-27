import pyglet

import resources
import potato
import needle
import score

game_window = pyglet.window.Window(800, 600)
game_window.set_caption("Poke")
game_window.set_mouse_visible(False)

score = score.Score()

bg = pyglet.sprite.Sprite(img=resources.bg_img)
potato = potato.Potato()
needle = needle.Needle(potato, score)

@game_window.event
def on_draw():
    game_window.clear()
    bg.draw()
    potato.draw()
    for eye in potato.eyes:
        eye.draw()
    needle.draw()
    pyglet.text.Label("Score: {}".format(score.eyes_poked),
                      x=50, y=50, color=(0,0,0,255)).draw()

def update(dt):
    if potato.opacity < 255:
        potato.opacity += 5
        for eye in potato.eyes:
            eye.opacity += 5
    else:
        potato.reinitialize()

game_window.push_handlers(needle)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
