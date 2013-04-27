import pyglet

pyglet.resource.path = ["../img", "../sounds"]
pyglet.resource.reindex()

# Images ----------------------------------------------------------------------
def _center_image(img):
    img.anchor_x = img.width/2
    img.anchor_y = img.height/2

bg_img = pyglet.resource.image("background.png")

potato_img = pyglet.resource.image("potato.png")
eye_img = pyglet.resource.image("eye.png")
eye_closed_img = pyglet.resource.image("eye_closed.png")
needle_img = pyglet.resource.image("needle.png")
crow_logo = pyglet.resource.image("feet.png")

_center_image(potato_img)
_center_image(eye_img)
_center_image(eye_closed_img)
needle_img.anchor_y = needle_img.height
needle_img.scale = 0.3
crow_logo.anchor_x = crow_logo.width

# Sounds ----------------------------------------------------------------------
ow = pyglet.resource.media("ow.mp3", streaming=False)
#oh = pyglet.resource.media("oh.mp3", streaming=False)
fanfare = pyglet.resource.media("fanfare.mp3", streaming=False)