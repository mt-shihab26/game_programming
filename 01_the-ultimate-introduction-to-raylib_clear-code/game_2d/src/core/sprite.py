from pyray import (
    WHITE,
    Vector2,
    Rectangle,
    draw_texture_v,
    load_texture,
    unload_texture,
    vector2_normalize,
)

from core.entity import Entity


class Sprite(Entity):
    def __init__(
        self, texture_path: str, position: Vector2, speed: float, direction: Vector2
    ) -> None:
        super().__init__()
        self.texture = load_texture(texture_path)
        self.position = position
        self.speed = speed
        self.direction = direction

    def close(self) -> None:
        unload_texture(self.texture)
        super().close()

    def update(self, delta_time: float) -> None:
        self.direction = vector2_normalize(self.direction)
        self.position.x += self.direction.x * self.speed * delta_time
        self.position.y += self.direction.y * self.speed * delta_time
        super().update(delta_time)

    def draw(self) -> None:
        super().draw()
        draw_texture_v(self.texture, self.position, WHITE)

    def rec(self):
        return Rectangle(
            self.position.x, self.position.y, self.texture.width, self.texture.height
        )
