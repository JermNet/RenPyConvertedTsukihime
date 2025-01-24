init python:

    # The size to scale everything by. Should be an integer.
    SCALE = 3

    config.screen_width = 256 * SCALE
    config.screen_height = 192 * SCALE

    theme.roundrect()

    style.default.font = "default.ttf"
    
transform bgpos:
    zoom SCALE

transform fgpos(x, y):
    zoom SCALE
    xpos (SCALE * x)
    ypos (SCALE * y)
    
