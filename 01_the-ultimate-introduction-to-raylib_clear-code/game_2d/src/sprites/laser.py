from os.path import join

from pyray import load_texture, unload_texture

from core.sprite import Sprite


class Laser(Sprite):
    def __init__(self) -> None:
        self.texture = load_texture(join("assets", "images", "laser.png"))

    def deinit(self) -> None:
        unload_texture(self.texture)

    def update(self, delta_time: float) -> None:
        pass

    def draw(self) -> None:
        pass
