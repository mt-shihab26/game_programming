from pyray import (
    WHITE,
    Texture,
    Vector2,
    draw_texture,
    draw_texture_v,
    load_texture,
    unload_texture,
    vector2_normalize,
)


class Sprite:
    def __init__(
        self, texture_path: str, position: Vector2, speed: float, direction: Vector2
    ) -> None:
        self.texture = load_texture(texture_path)
        self.position = position
        self.speed = speed
        self.direction = direction

    def close(self) -> None:
        unload_texture(self.texture)

    def update(self, delta_time: float) -> None:
        self.direction = vector2_normalize(self.direction)
        self.position.x += self.direction.x * self.speed * delta_time
        self.position.y += self.direction.y * self.speed * delta_time

    def draw(self) -> None:
        draw_texture_v(self.texture, self.position, WHITE)
