from pyray import (
    WHITE,
    Texture,
    Vector2,
    draw_texture,
    draw_texture_ex,
    get_screen_height,
    get_screen_width,
    load_music_stream,
    load_texture,
    play_music_stream,
    unload_music_stream,
    unload_texture,
    update_music_stream,
)
from random import randint, uniform

from core.paths import music_sound_path, star_image_path
from core.entity import Entity


class Background(Entity):
    def __init__(
        self,
        texture: Texture,
    ) -> None:
        self.stream = load_music_stream(music_sound_path())
        play_music_stream(self.stream)
        self.texture = texture
        self.stars = [
            (
                Vector2(
                    randint(0, get_screen_width()), randint(0, get_screen_height())
                ),
                uniform(0.5, 1.5),
            )
            for i in range(30)
        ]

    def close(self) -> None:
        unload_music_stream(self.stream)
        unload_texture(self.texture)

    def update(self, delta_time: float) -> None:
        update_music_stream(self.stream)

    def draw(self) -> None:
        for star in self.stars:
            draw_texture_ex(self.texture, star[0], 0, star[1], WHITE)
