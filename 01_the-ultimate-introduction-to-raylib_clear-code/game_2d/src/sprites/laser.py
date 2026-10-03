from pyray import play_sound

from core.sprite import Sprite
from pyray import Sound, Texture, Vector2

from core.config import LASER_SPEED


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
