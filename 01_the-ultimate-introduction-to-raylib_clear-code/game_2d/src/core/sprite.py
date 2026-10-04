from pyray import get_screen_height, get_screen_width, draw_texture_v, vector2_normalize

from core.entity import Entity
from pyray import Texture, Vector2, Rectangle

from pyray import WHITE


class Sprite(Entity):
    def __init__(
        self,
        texture: Texture,
        position: Vector2 = Vector2(0, 0),
        speed: float = 0,
        direction: Vector2 = Vector2(0, 0),
    ) -> None:
        super().__init__()

        self.texture = texture
        self.position = position
        self.speed = speed
        self.direction = direction
        self.size = Vector2(texture.width, texture.height)
        self.radius = self.size.y / 2

    def close(self) -> None:
        super().close()

    def update(self, delta_time: float) -> None:
        self.direction = vector2_normalize(self.direction)
        self.position.x += self.direction.x * self.speed * delta_time
        self.position.y += self.direction.y * self.speed * delta_time

        super().update(delta_time)

    def draw(self) -> None:
        super().draw()
        draw_texture_v(self.texture, self.position, WHITE)

    def constraint(self) -> Vector2:
        width = get_screen_width()
        height = get_screen_height()
        x = max(0, min(self.position.x, width - self.size.x))
        y = max(0, min(self.position.y, height - self.size.y))
        return Vector2(x, y)

    def rectangle(self):
        return Rectangle(self.position.x, self.position.y, self.size.x, self.size.y)

    def center(self) -> Vector2:
        return Vector2(
            self.position.x + (self.size.x / 2), self.position.y + (self.size.y / 2)
        )
