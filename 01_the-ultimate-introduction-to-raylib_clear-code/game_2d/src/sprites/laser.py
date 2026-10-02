from core.paths import laser_image_path, laser_sound_path
from dataclasses import dataclass
from typing import override
from pyray import draw_texture_v, load_sound, load_texture, play_sound
from pyray import unload_sound, unload_texture

from core.sprite import Sprite
from core.timer import Timer
from typing import Text
from pyray import Rectangle, Sound, Texture, Vector2

from core.config import LASER_SPEED
from pyray import WHITE


class Laser(Sprite):
    def __init__(self, texture: Texture, sound: Sound, position: Vector2) -> None:
        super().__init__(
            texture=texture,
            position=Vector2(
                position.x - (texture.width / 2), position.y - texture.height
            ),
            speed=LASER_SPEED,
            direction=Vector2(0, -1),
        )
        play_sound(sound)

    def close(self) -> None:
        super().close()

    def update(self, delta_time: float) -> None:
        super().update(delta_time)

    def draw(self) -> None:
        draw_texture_v(self.texture, self.position, WHITE)
