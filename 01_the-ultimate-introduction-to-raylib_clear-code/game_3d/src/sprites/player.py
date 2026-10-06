from pyray import Model, Vector3
from core.sprite import Sprite


class Player(Sprite):
    def __init__(self, model: Model) -> None:
        super().__init__(
            model=model,
            position=Vector3(0, 0, 7.5),
            direction=Vector3(0, 0, 0),
            speed=0,
        )
