import pyglet
from pyglet import shapes
from pyglet.window import key

from ichigojam import Std15
from ichigojam import DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT
import random

def main():
    global frame
    global x
    global running

    window = pyglet.window.Window(512,384)
    std15 = Std15(512, 384, 32, 24)

    frame = 0
    x = 15
    running = True

    @window.event
    def on_key_press(symbol, modifiers):
        global x
        if symbol == key.LEFT:
            x -= 1
        elif symbol == key.RIGHT:
            x += 1

    def on_update(dt):
        global frame
        global x
        global running
        
        if not running:
            return
        if frame % 5 == 0:
            std15.locate(x, 5)
            std15.putc(ord('0'))
            std15.locate(random.randrange(32), 23)
            std15.putc(ord('*'))
            std15.scroll(DIR_UP)
            if std15.scr(x,5) != 0:
                std15.locate(0,23)
                std15.putstr("Game Over...")
                std15.putnum(frame)
                running = False
        frame += 1
        
    @window.event
    def on_draw():
        std15.draw_screen(window)

    pyglet.clock.schedule_interval(on_update,1/60.0)
    pyglet.app.run()


if __name__ == "__main__":
    main()
