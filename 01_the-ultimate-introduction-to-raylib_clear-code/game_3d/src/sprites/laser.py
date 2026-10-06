from pyray import Model, Sound, Vector3, play_sound
from core.sprite import Sprite

from pyray import RED


class Laser(Sprite):
    def __init__(self, model: Model, position: Vector3, sound: Sound) -> None:
        super().__init__(
            model,
            position=Vector3(position.x, position.y, position.z),
            direction=Vector3(0, 0, -1),
            speed=12,
            scale=1,
            color=RED,
        )
        play_sound(sound)
