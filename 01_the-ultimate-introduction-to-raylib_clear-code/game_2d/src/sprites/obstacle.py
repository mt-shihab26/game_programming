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

from core.config import METEOR_SPEED_RANGE, METEOR_TIMER_DURATION
from core.sprite import Sprite
from core.timer import Timer


class Obstacle(Sprite):
    def __init__(self) -> None:
        self.texture = load_texture(join("assets", "images", "meteor.png"))
        self.items = []
        self.timer = Timer(
            METEOR_TIMER_DURATION,
            repeat=True,
            autostart=True,
            func=self.__add_new_position,
        )

    def deinit(self) -> None:
        unload_texture(self.texture)

    def update(self, delta_time: float) -> None:
        self.timer.update()
        for item in self.items:
            item.position.y += item.speed * delta_time

    def draw(self) -> None:
        for item in self.items:
            draw_texture_v(self.texture, item.position, WHITE)

    def __get_new_position(self):
        random_x = randint(0, get_screen_width() - self.texture.width)
        return {
            "position": Vector2(random_x, -self.texture.height),
            "speed": randint(METEOR_SPEED_RANGE[0], METEOR_SPEED_RANGE[1]),
        }

    def __add_new_position(self):
        random_x = randint(0, get_screen_width() - self.texture.width)
        self.items.append(
            {
                "position": Vector2(random_x, -self.texture.height),
                "speed": randint(METEOR_SPEED_RANGE[0], METEOR_SPEED_RANGE[1]),
            }
        )
