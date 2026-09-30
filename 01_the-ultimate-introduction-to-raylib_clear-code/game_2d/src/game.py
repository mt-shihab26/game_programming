from pyray import (
    clear_background,
    end_drawing,
    get_frame_time,
    init_window,
    is_window_resized,
    close_window,
    window_should_close,
    begin_drawing,
)

from config import BG_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT
from player import Player


class Game:
    def __init__(self) -> None:
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Game 2D")
        self.__wait_for_window_size()
        self.player = Player()

    def __deinit(self) -> None:
        self.player.deinit()
        close_window()

    def run(self) -> None:
        while not window_should_close():
            delta_time = get_frame_time()
            self.__update(delta_time)
            self.__draw()
        self.__deinit()

    def __update(self, delta_time: float) -> None:
        self.player.update(delta_time)

    def __draw(self) -> None:
        begin_drawing()
        clear_background(BG_COLOR)
        self.player.draw()
        end_drawing()

    def __wait_for_window_size(self) -> None:
        # Tiling WMs (Hyprland) resize the window only after the first frames are drawn
        for _ in range(10):
            begin_drawing()
            clear_background(BG_COLOR)
            end_drawing()
            if is_window_resized():
                break
