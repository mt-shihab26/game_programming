from pyray import (
    WHITE,
    Vector2,
    draw_texture_v,
    get_screen_height,
    get_screen_width,
    load_texture,
    unload_texture,
)
from core.config import METEOR_SPEED_RANGE, METEOR_TIMER_DURATION
from core.paths import meteor_image_path
from core.sprite import Sprite
from core.timer import Timer

from random import randint
from dataclasses import dataclass
from typing import override


@dataclass
class Meteor:
    position: Vector2
    speed: int

    @override
    def __repr__(self) -> str:
        return (
            f"Meteor(x={self.position.x:.1f}, y={self.position.y:.1f}, "
            f"speed={self.speed})"
        )


class Obstacle(Sprite):
    def __init__(self) -> None:
        self.texture = load_texture(meteor_image_path())
        self.meteors: list[Meteor] = []
        self.timer = Timer(
            METEOR_TIMER_DURATION,
            repeat=True,
            autostart=True,
            func=self.__add_new_meteor,
        )

    def close(self) -> None:
        unload_texture(self.texture)

    def update(self, delta_time: float) -> None:
        self.timer.update()
        for meteor in self.meteors:
            meteor.position.y += meteor.speed * delta_time
        meteors: list[Meteor] = []
        for meteor in self.meteors:
            if meteor.position.y <= get_screen_height():
                meteors.append(meteor)
        self.meteors = meteors

    def draw(self) -> None:
        for meteor in self.meteors:
            draw_texture_v(self.texture, meteor.position, WHITE)

    def __add_new_meteor(self) -> None:
        self.meteors.append(
            Meteor(self.__get_new_position(), randint(*METEOR_SPEED_RANGE))
        )

    def __get_new_position(self) -> Vector2:
        return Vector2(
            randint(0, max(0, get_screen_width() - self.texture.width)),
            -self.texture.height,
        )
