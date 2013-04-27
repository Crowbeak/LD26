import pyglet

import resources
import potato
import needle
import score
import intro

game_window = pyglet.window.Window(800, 600)
game_window.set_caption("Poke")
game_window.set_mouse_visible(False)

title = intro.Title()

score = score.Score()

bg = pyglet.sprite.Sprite(img=resources.bg_img)
potato = potato.Potato()
needle = needle.Needle(title, potato, score)

@game_window.event
def on_draw():
    game_window.clear()
    bg.draw()
    if title.timer > 0:
        title.draw()
        title.game_title.draw()
        title.credits.draw()
    else:
        potato.draw()
        for eye in potato.eyes:
            eye.draw()
        needle.draw()
    
        #Draw score and time remaining.
        if score.timer >= 0:
            pyglet.text.Label("{}".format(score.timer), x=10, y=30,
                              color=(0,0,0,255)).draw()
            pyglet.text.Label("Score: {}".format(score.eyes_poked),
                              x=10, y=10, color=(0,0,0,255)).draw()
        else:
            pyglet.text.Label("Final Score: {}".format(score.eyes_poked),
                              anchor_x="center", anchor_y="center",
                              font_size=36, x=400, y=400,
                              color=(0,0,0,255)).draw()
            pyglet.text.Label("Press ESC to exit.", anchor_x="center",
                              anchor_y="center", x=400, y=350,
                              color=(0,0,0,255)).draw()
            pyglet.text.Label("Thank you for playing Poke!",
                              anchor_x="center", anchor_y="center",
                              font_size=20, x=400, y=2750,
                              color=(0,0,0,255)).draw()

def update(dt):
    if title.timer > 0:
        title.timer -= 1
    else:
        if potato.opacity < 255:
            potato.opacity += 5
            for eye in potato.eyes:
                eye.opacity += 5
        else:
            potato.reinitialize()
    
        score.timer -= 1
    
        if score.timer == 0:
            resources.fanfare.play()
        if score.timer <= 0:
            potato.visible = False
            for eye in potato.eyes:
                eye.visible = False

game_window.push_handlers(needle)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
