from pyray import get_screen_width
from random import randint

from pyray import Vector2
from core.sprite import Sprite

from core.config import METEOR_SPEED_RANGE


class Meteor(Sprite):
    def __init__(
        self,
        texture,
    ) -> None:
        super().__init__(
            texture=texture,
            position=Vector2(
                randint(0, max(0, get_screen_width() - texture.width)),
                -texture.height,
            ),
            speed=randint(*METEOR_SPEED_RANGE),
            direction=Vector2(0, 1),
        )

    def close(self) -> None:
        super().close()

    def update(self, delta_time: float) -> None:
        super().update(delta_time)

    def draw(self) -> None:
        super().draw()
