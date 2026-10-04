from random import randint, uniform
from pyray import draw_texture_ex, get_screen_height, get_screen_width
from pyray import play_music_stream, update_music_stream

from pyray import Texture, Vector2, Music
from core.entity import Entity

from pyray import WHITE


class Background(Entity):
    def __init__(self, texture: Texture, music: Music) -> None:
        self.texture = texture
        self.music = music

        self.stars = [
            (
                Vector2(
                    randint(0, get_screen_width()), randint(0, get_screen_height())
                ),
                uniform(0.5, 1.6),
            )
            for i in range(30)
        ]

        play_music_stream(self.music)

    def close(self) -> None:
        pass

    def update(self, delta_time: float) -> None:
        update_music_stream(self.music)

    def draw(self) -> None:
        for star in self.stars:
            draw_texture_ex(self.texture, star[0], 0, star[1], WHITE)
