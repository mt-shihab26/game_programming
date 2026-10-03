from pyray import WHITE, Texture, Vector2, draw_texture_v

from core.entity import Entity


class Explosion(Entity):
    def __init__(self, textures: list[Texture], position: Vector2) -> None:
        super().__init__()

        self.textures = textures
        texture = self.textures[0]
        self.size = Vector2(texture.width, texture.height)
        self.position = Vector2(
            position.x - self.size.x / 2, position.y - self.size.y / 2
        )
        self.index = 0

    def draw(self) -> None:
        super().draw()
        draw_texture_v(self.textures[self.index], self.position, WHITE)
