from typing import override

from pyray import (
    WHITE,
    Vector2,
    draw_texture_v,
    get_screen_height,
    load_texture,
    unload_texture,
)
from dataclasses import dataclass

from core.config import LASER_SPEED
from core.paths import laser_image_path
from core.sprite import Sprite
from core.timer import Timer
from sprites import player


@dataclass
class Laser:
    position: Vector2
    speed: int


class Weapon:
    def __init__(self) -> None:
        self.texture = load_texture(laser_image_path())
        self.lasers: list[Laser] = []

    def deinit(self) -> None:
        unload_texture(self.texture)

    def update(
        self, delta_time: float, player_center_x: float, player_y: float
    ) -> None:
        laser_x = player_center_x - (self.texture.width / 2)

        if not self.__has_laser_at_x(laser_x):
            self.lasers.append(
                Laser(
                    Vector2(
                        laser_x,
                        player_y - self.texture.height,
                    ),
                    LASER_SPEED,
                )
            )

        for laser in self.lasers:
            laser.position.y -= laser.speed * delta_time

        lasers: list[Laser] = []
        for laser in self.lasers:
            if 0 <= laser.position.y:
                lasers.append(laser)
        self.lasers = lasers

        print(len(self.lasers))

    def draw(self) -> None:
        for laser in self.lasers:
            draw_texture_v(self.texture, laser.position, WHITE)

    def __has_laser_at_x(self, laser_x: float) -> bool:
        for laser in self.lasers:
            if laser.position.x == laser_x:
                return True
        return False
