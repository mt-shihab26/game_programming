from pyray import draw_texture_v, play_sound

from core.entity import Entity
from pyray import Sound, Texture, Vector2

from pyray import WHITE


class Explosion(Entity):
    def __init__(
        self, textures: list[Texture], position: Vector2, sound: Sound
    ) -> None:
        super().__init__()

        self.textures = textures
        texture = self.textures[0]
        self.size = Vector2(texture.width, texture.height)
        self.position = Vector2(
            position.x - self.size.x / 2, position.y - self.size.y / 2
        )
        self.index = 0
        self.len = len(textures)
        self.speed = 50

        play_sound(sound)

    def update(self, delta_time: float) -> None:
        super().update(delta_time)
        self.index += self.speed * delta_time

    def draw(self) -> None:
        super().draw()
        if self.index < self.len:
            draw_texture_v(self.textures[int(self.index)], self.position, WHITE)
