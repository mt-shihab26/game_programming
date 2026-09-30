from pyray import (
    clear_background,
    end_drawing,
    get_frame_time,
    init_window,
    close_window,
    window_should_close,
    begin_drawing,
)

from config import BG_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT
from player import Player


class Game:
    def __init__(self) -> None:
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Game 2D")
        self.player = Player()

    def deinit(self) -> None:
        self.player.deinit()
        close_window()

    def update(self, delta_time: float) -> None:
        self.player.update(delta_time)

    def draw(self) -> None:
        begin_drawing()
        clear_background(BG_COLOR)
        self.player.draw()
        end_drawing()

    def run(self) -> None:
        while not window_should_close():
            delta_time = get_frame_time()
            self.update(delta_time)
            self.draw()
        self.deinit()
