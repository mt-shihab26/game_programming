from pyray import (
    WHITE,
    Vector2,
    draw_texture_v,
    get_screen_height,
    load_texture,
    unload_texture,
)

from core.config import LASER_SPEED
from core.paths import laser_image_path
from core.sprite import Sprite
from core.timer import Timer
from sprites import player

from dataclasses import dataclass
from typing import override


@dataclass
class Laser:
    position: Vector2
    speed: int

    @override
    def __repr__(self) -> str:
        return (
            f"Laser(x={self.position.x:.1f}, y={self.position.y:.1f}, "
            f"speed={self.speed})"
        )


class Weapon:
    def __init__(self) -> None:
        self.texture = load_texture(laser_image_path())
        self.lasers: list[Laser] = []
        self.timer = Timer(0.5, repeat=True, autostart=True)

    def close(self) -> None:
        unload_texture(self.texture)

    def update(
        self, delta_time: float, player_center_x: float, player_y: float
    ) -> None:
        if self.timer.update():
            laser_x = player_center_x - (self.texture.width / 2)
            laser_y = player_y - self.texture.height
            self.lasers.append(
                Laser(
                    Vector2(
                        laser_x,
                        laser_y,
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

    def draw(self) -> None:
        for laser in self.lasers:
            draw_texture_v(self.texture, laser.position, WHITE)
