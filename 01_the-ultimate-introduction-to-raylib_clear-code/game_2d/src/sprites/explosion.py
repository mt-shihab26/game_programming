from pyray import load_texture, unload_texture

from core.paths import explosion_image_paths
from core.sprite import Sprite


class Explosion(Sprite):
    def __init__(self) -> None:
        self.index = 0
        self.textures = []
        for image_path in explosion_image_paths():
            self.textures.append(load_texture(image_path))

    def close(self) -> None:
        for texture in self.textures:
            unload_texture(texture)

    def update(self, delta_time: float) -> None:
        pass

    def draw(self) -> None:
        pass
