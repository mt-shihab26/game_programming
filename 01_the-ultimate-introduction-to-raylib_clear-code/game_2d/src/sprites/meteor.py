from pyray import draw_texture_pro, get_screen_width
from random import randint, uniform

from pyray import Vector2
from core.sprite import Sprite
from pyray import Rectangle

from pyray import WHITE
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
        self.rotation = 0
        self.source = Rectangle(0, 0, self.size.x, self.size.y)

    def update(self, delta_time: float) -> None:
        super().update(delta_time)
        self.rotation += 50 * delta_time

    def draw(self) -> None:
        draw_texture_pro(
            self.texture,
            self.source,
            self.rec(),
            Vector2(self.size.x / 2, self.size.y / 2),
            self.rotation,
            WHITE,
        )
