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
    
    #Draw score and time remaining.
    if score.time >= 0:
        pyglet.text.Label("{}".format(score.time), x=10, y=30,
                          color=(0,0,0,255)).draw()
        pyglet.text.Label("Score: {}".format(score.eyes_poked),
                          x=10, y=10, color=(0,0,0,255)).draw()
    else:
        pyglet.text.Label("Final Score: {}".format(score.eyes_poked),
                          anchor_x="center", anchor_y="center", font_size=36,
                          x=400, y=300, color=(0,0,0,255)).draw()
        pyglet.text.Label("Press ESC to exit.", anchor_x="center",
                          anchor_y="center", x=400, y=250,
                          color=(0,0,0,255)).draw()

def update(dt):
    if potato.opacity < 255:
        potato.opacity += 5
        for eye in potato.eyes:
            eye.opacity += 5
    else:
        potato.reinitialize()
    
    score.time -= 1
    
    if score.time == 0:
        resources.fanfare.play()
    if score.time <= 0:
        potato.visible = False
        for eye in potato.eyes:
            eye.visible = False

game_window.push_handlers(needle)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
