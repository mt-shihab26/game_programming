from pyray import draw_model, vector3_normalize

from pyray import Model, Vector3
from core.sprite import Sprite
from core.entity import Entity

from pyray import WHITE


class Laser(Sprite):
    def __init__(self, model: Model) -> None:
        super().__init__(
            model,
            position=Vector3(0, 0, 0),
            direction=Vector3(0, 0, -1),
            speed=5,
            scale=1,
        )
