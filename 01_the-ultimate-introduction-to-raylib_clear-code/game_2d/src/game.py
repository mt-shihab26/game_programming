from config import BG_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT

from pyray import (
    clear_background,
    end_drawing,
    init_window,
    close_window,
    window_should_close,
    begin_drawing,
)


class Game:
    def run(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Game 2D")
        while not window_should_close():
            begin_drawing()
            clear_background(BG_COLOR)
            end_drawing()
        close_window()
