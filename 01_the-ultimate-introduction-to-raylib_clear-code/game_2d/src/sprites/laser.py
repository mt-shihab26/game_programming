
from pyray import load_texture, unload_texture

from core.paths import laser_image_path
from core.sprite import Sprite


class Laser(Sprite):
    def __init__(self) -> None:
        self.texture = load_texture(laser_image_path())

    def deinit(self) -> None:
        unload_texture(self.texture)

    def update(self, delta_time: float) -> None:
        pass

    def draw(self) -> None:
        pass
