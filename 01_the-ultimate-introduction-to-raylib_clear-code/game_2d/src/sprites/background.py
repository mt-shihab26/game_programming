from pyray import (
    WHITE,
    draw_texture,
    get_screen_height,
    get_screen_width,
    load_music_stream,
    load_texture,
    play_music_stream,
    unload_music_stream,
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
        self.width = get_screen_width() / len(STAR_MAP[0])
        self.height = get_screen_height() / len(STAR_MAP)

    def close(self) -> None:
        unload_music_stream(self.stream)

    def update(self, delta_time: float) -> None:
        update_music_stream(self.stream)
        for y, row in enumerate(STAR_MAP):
            for x, col in enumerate(row):
                if col == 1:
                    draw_texture(
                        self.texture, int(x * self.width), int(y * self.height), WHITE
                    )
