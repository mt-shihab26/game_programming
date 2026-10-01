from pyray import (
    RED,
    clear_background,
    close_audio_device,
    end_drawing,
    get_frame_time,
    init_audio_device,
    init_window,
    is_window_resized,
    close_window,
    window_should_close,
    begin_drawing,
)

from core.config import BG_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT
from core.sprite import Sprite
from sprites.music import Music
from sprites.player import Player
from sprites.obstacle import Obstacle
from sprites.weapon import Weapon


def init() -> list[Sprite]:
    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Game 2D")
    init_audio_device()
    wait_for_window_size()
    return [Music(), Obstacle(), Player()]


def deinit(sprites: list[Sprite]) -> None:
    for sprite in sprites:
        sprite.deinit()
    close_audio_device()
    close_window()


def update(sprites: list[Sprite], delta_time: float) -> None:
    for sprite in sprites:
        sprite.update(delta_time)


def draw(sprites: list[Sprite]) -> None:
    begin_drawing()
    clear_background(BG_COLOR)
    for sprite in sprites:
        sprite.draw()
    end_drawing()


def wait_for_window_size() -> None:
    # Tiling WMs (Hyprland) resize the window only after the first frames are drawn
    for _ in range(10):
        begin_drawing()
        clear_background(RED)
        end_drawing()
        if is_window_resized():
            break


def main() -> None:
    sprites = init()
    while not window_should_close():
        delta_time = get_frame_time()
        update(sprites, delta_time)
        draw(sprites)
    deinit(sprites)


if __name__ == "__main__":
    main()
