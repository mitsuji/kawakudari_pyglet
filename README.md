# kawakudari-pyglet

This project implements part of the [std15.h](https://github.com/IchigoJam/c4ij/blob/master/src/std15.h) API (from [c4ij](https://github.com/IchigoJam/c4ij)) with [pyglet](https://pyglet.readthedocs.io/en/latest/), and [Kawakudari Game](https://ichigojam.github.io/print/en/KAWAKUDARI.html) on top of it.

It will allow programming for [IchigoJam](https://ichigojam.net/index-en.html)-like targets that display [IchigoJam FONT](https://mitsuji.github.io/ichigojam-font.json/) on screen using a Python programming language.
```
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

```

## Prerequisite

* [Download](https://www.python.org/downloads/) and install Python suitable for your environment.
* [Download](https://pyglet.readthedocs.io/en/latest/programming_guide/installation.html) and install pyglet library.

```
$ pip3 install pyglet --user
```


## How to use

To run it
```
$ python3 kawakudari.py
```


## License
[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
[CC BY](https://creativecommons.org/licenses/by/4.0/) [mitsuji.org](https://mitsuji.org)

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
