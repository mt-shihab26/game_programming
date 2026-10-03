from pyray import get_screen_width
from random import randint, uniform

from pyray import Vector2
from core.sprite import Sprite

from core.config import METEOR_SPEED_RANGE


class Meteor(Sprite):
    def __init__(
        self,
        texture,
    ) -> None:
        position = Vector2(
            randint(0, max(0, get_screen_width() - texture.width)), -texture.height
        )
        super().__init__(
            texture=texture,
            position=position,
            speed=randint(*METEOR_SPEED_RANGE),
            direction=Vector2(uniform(-0.5, 0.5), 1),
        )
