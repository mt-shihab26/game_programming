from dataclasses import dataclass
from typing import override

from pyray import (
    WHITE,
    Texture,
    Vector2,
    draw_text,
    draw_texture,
    draw_texture_v,
    load_texture,
    unload_texture,
)

from core.paths import explosion_image_paths
from core.sprite import Sprite


@dataclass
class Distory:
    def __init__(self, position: Vector2) -> None:
        self.index = 0
        self.position = position

    @override
    def __repr__(self) -> str:
        return (
            f"Distory(x={self.position.x:.1f}, y={self.position.y:.1f}, "
            f"index={self.index})"
        )


class Explosion(Sprite):
    def __init__(self) -> None:
        self.textures: list[Texture] = []
        for image_path in explosion_image_paths():
            self.textures.append(load_texture(image_path))
        self.frames = len(self.textures)
        self.distories: list[Distory] = []

    def close(self) -> None:
        for texture in self.textures:
            unload_texture(texture)

    def add(self, position: Vector2):
        self.distories.append(Distory(position))

    def update(self, delta_time: float) -> None:
        for distory in self.distories:
            distory.index += int(1 * delta_time)
        distories: list[Distory] = []
        for distory in self.distories:
            if distory.index < self.frames:
                distories.append(distory)
        self.distories = distories
        print(self.distories)

    def draw(self) -> None:
        for distory in self.distories:
            draw_texture_v(self.textures[distory.index], distory.position, WHITE)
