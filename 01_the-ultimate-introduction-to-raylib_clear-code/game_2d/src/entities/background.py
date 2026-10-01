from pyray import (
    WHITE,
    draw_texture,
    get_screen_height,
    get_screen_width,
    load_music_stream,
    load_texture,
    play_music_stream,
    unload_music_stream,
    unload_texture,
    update_music_stream,
)

from core.paths import music_sound_path, star_image_path
from core.entity import Entity

STAR_MAP = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
]


class Background(Entity):
    def __init__(self) -> None:
        self.stream = load_music_stream(music_sound_path())
        play_music_stream(self.stream)
        self.texture = load_texture(star_image_path())

    def close(self) -> None:
        unload_music_stream(self.stream)
        unload_texture(self.texture)

    def update(self, delta_time: float) -> None:
        update_music_stream(self.stream)

    def draw(self) -> None:
        width = get_screen_width() / len(STAR_MAP[0])
        height = get_screen_height() / len(STAR_MAP)
        for y, row in enumerate(STAR_MAP):
            for x, col in enumerate(row):
                if col == 1:
                    draw_texture(self.texture, int(x * width), int(y * height), WHITE)
