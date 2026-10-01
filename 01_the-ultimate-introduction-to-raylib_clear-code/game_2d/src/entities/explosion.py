from typing import override

from pyray import (
    WHITE,
    Texture,
    Vector2,
    draw_texture_v,
    load_sound,
    load_texture,
    play_sound,
    unload_sound,
    unload_texture,
)

from core.paths import explosion_image_paths, explosion_sound_path
from core.entity import Entity


class Distory:
    def __init__(self, position: Vector2) -> None:
        self.index = 0.0
        self.position = position

    @override
    def __repr__(self) -> str:
        return (
            f"Distory(x={self.position.x:.1f}, y={self.position.y:.1f}, "
            f"index={self.index})"
        )


class Explosion(Entity):
    def __init__(self) -> None:
        self.textures: list[Texture] = []
        for image_path in explosion_image_paths():
            self.textures.append(load_texture(image_path))
        self.frames = len(self.textures)
        self.distories: list[Distory] = []
        self.speed = 50
        self.sound = load_sound(explosion_sound_path())

    def close(self) -> None:
        for texture in self.textures:
            unload_texture(texture)
        unload_sound(self.sound)

    def add(self, position: Vector2):
        self.distories.append(Distory(position))
        play_sound(self.sound)

    def update(self, delta_time: float) -> None:
        for distory in self.distories:
            distory.index += self.speed * delta_time
        distories: list[Distory] = []
        for distory in self.distories:
            if int(distory.index) < self.frames:
                distories.append(distory)
        self.distories = distories

    def draw(self) -> None:
        for distory in self.distories:
            texture = self.textures[int(distory.index)]
            draw_texture_v(
                texture,
                Vector2(
                    distory.position.x - (texture.width / 2),
                    distory.position.y - (texture.height / 2),
                ),
                WHITE,
            )
