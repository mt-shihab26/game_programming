from pyray import (
    clear_background,
    close_audio_device,
    end_drawing,
    get_frame_time,
    init_audio_device,
    init_window,
    is_window_resized,
    close_window,
    load_audio_stream,
    window_should_close,
    begin_drawing,
)

from core.config import BG_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT
from sprites.music import Music
from sprites.player import Player
from sprites.obstacle import Obstacle


class Game:
    def __init__(self) -> None:
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Game 2D")
        init_audio_device()
        self.__wait_for_window_size()
        self.sprites = [Obstacle(), Player(), Music()]

    def __deinit(self) -> None:
        for sprite in self.sprites:
            sprite.deinit()
        close_audio_device()
        close_window()

    def run(self) -> None:
        while not window_should_close():
            delta_time = get_frame_time()
            self.__update(delta_time)
            self.__draw()
        self.__deinit()

    def __update(self, delta_time: float) -> None:
        for sprite in self.sprites:
            sprite.update(delta_time)

    def __draw(self) -> None:
        begin_drawing()
        clear_background(BG_COLOR)
        for sprite in self.sprites:
            sprite.draw()
        end_drawing()

    def __wait_for_window_size(self) -> None:
        # Tiling WMs (Hyprland) resize the window only after the first frames are drawn
        for _ in range(10):
            begin_drawing()
            clear_background(BG_COLOR)
            end_drawing()
            if is_window_resized():
                break


game = Game()

game.run()
