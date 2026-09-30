from os.path import join
from pyray import (
    WHITE,
    Vector2,
    draw_texture_v,
    get_screen_width,
    load_texture,
    unload_texture,
)
from random import randint, randrange

from core.config import METEOR_SPEED_RANGE
from core.sprite import Sprite


class Obstacle(Sprite):
    def __init__(self) -> None:
        self.texture = load_texture(join("assets", "images", "meteor.png"))
        self.position = Vector2(
            randint(0, get_screen_width() - self.texture.width), -self.texture.height
        )

    def deinit(self) -> None:
        unload_texture(self.texture)

    def update(self, delta_time: float) -> None:
        self.position.y += (
            randint(METEOR_SPEED_RANGE[0], METEOR_SPEED_RANGE[1]) * delta_time
        )

    def draw(self) -> None:
        draw_texture_v(self.texture, self.position, WHITE)
