from pyray import (
    WHITE,
    Rectangle,
    Vector2,
    draw_texture_v,
    load_sound,
    load_texture,
    play_sound,
    unload_sound,
    unload_texture,
)

from core.config import LASER_SPEED
from core.paths import laser_image_path, laser_sound_path
from core.timer import Timer

from dataclasses import dataclass
from typing import override


@dataclass
class Laser:
    position: Vector2
    speed: int
    width: int
    height: int

    @override
    def __repr__(self) -> str:
        return (
            f"Laser(x={self.position.x:.1f}, y={self.position.y:.1f}, "
            f"speed={self.speed})"
        )

    def rec(self):
        return Rectangle(self.position.x, self.position.y, self.width, self.height)


class Weapon:
    def __init__(self) -> None:
        self.texture = load_texture(laser_image_path())
        self.sound = load_sound(laser_sound_path())
        self.lasers: list[Laser] = []
        self.timer = Timer(0.5, repeat=True, autostart=True)

    def close(self) -> None:
        unload_texture(self.texture)
        unload_sound(self.sound)

    def update(
        self, delta_time: float, player_center_x: float, player_y: float
    ) -> None:
        if self.timer.update():
            self.shoot_laser(player_center_x, player_y)

        for laser in self.lasers:
            laser.position.y -= laser.speed * delta_time

        lasers: list[Laser] = []
        for laser in self.lasers:
            if 0 <= laser.position.y:
                lasers.append(laser)
        self.lasers = lasers

    def shoot_laser(self, player_center_x: float, player_y: float):
        laser_x = player_center_x - (self.texture.width / 2)
        laser_y = player_y - self.texture.height
        self.lasers.append(
            Laser(
                Vector2(
                    laser_x,
                    laser_y,
                ),
                LASER_SPEED,
                self.texture.width,
                self.texture.height,
            )
        )
        play_sound(self.sound)

    def draw(self) -> None:
        for laser in self.lasers:
            draw_texture_v(self.texture, laser.position, WHITE)
