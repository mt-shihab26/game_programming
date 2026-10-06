from pyray import draw_model, get_model_bounding_box, vector3_normalize

from pyray import Color, Model, Vector3
from core.entity import Entity

from pyray import WHITE


class Sprite(Entity):
    def __init__(
        self,
        model: Model,
        position: Vector3,
        direction: Vector3,
        speed: float,
        scale: float = 1.0,
        color: Color = WHITE,
    ) -> None:
        self.model = model
        self.position = position
        self.scale = scale
        self.direction = direction
        self.speed = speed
        self.color = color

    def update(self, dt: float) -> None:
        self.direction = vector3_normalize(self.direction)
        self.position.x += self.direction.x * self.speed * dt
        self.position.y += self.direction.y * self.speed * dt
        self.position.z += self.direction.z * self.speed * dt

    def draw(self) -> None:
        draw_model(self.model, self.position, self.scale, self.color)

    def size(self) -> dict[str, float]:
        box = get_model_bounding_box(self.model)
        return {
            "width": (box.max.x - box.min.x) * self.scale,
            "height": (box.max.y - box.min.y) * self.scale,
            "depth": (box.max.z - box.min.z) * self.scale,
        }
