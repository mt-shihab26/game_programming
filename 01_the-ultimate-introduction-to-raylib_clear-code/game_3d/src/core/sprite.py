from pyray import (
    RED,
    Model,
    Vector3,
    gen_mesh_sphere,
    load_model_from_mesh,
    normalize,
    unload_model,
    draw_model,
    vector3_normalize,
)


from core.entity import Entity
from pyray import Texture, Vector2, Rectangle

from pyray import WHITE


class Sprite(Entity):
    def __init__(
        self,
        model: Model,
        position: Vector3,
        direction: Vector3,
        speed: float,
        scale: float = 1.0,
    ) -> None:
        self.model = model
        self.position = position
        self.scale = scale
        self.direction = direction
        self.speed = speed

    def update(self, dt: float) -> None:
        self.direction = vector3_normalize(self.direction)
        self.position.x += self.direction.x * self.speed * dt
        self.position.y += self.direction.y * self.speed * dt
        self.position.z += self.direction.z * self.speed * dt

    def draw(self) -> None:
        draw_model(self.model, self.position, self.scale, WHITE)
