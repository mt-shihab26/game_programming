from pyray import draw_model, get_model_bounding_box, vector3_normalize
from pyray import vector3_add, vector3_scale

from pyray import Color, Model, Vector3, BoundingBox

from core.entity import Entity

from pyray import WHITE


class Sprite(Entity):
    def __init__(
        self,
        model: Model,
        position: Vector3 = Vector3(0, 0, 0),
        direction: Vector3 = Vector3(0, 0, 0),
        speed: float = 0,
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

    def get_bounding_box(self) -> BoundingBox:
        bbox = get_model_bounding_box(self.model)
        return BoundingBox(
            vector3_add(self.position, vector3_scale(bbox.min, self.scale)),
            vector3_add(self.position, vector3_scale(bbox.max, self.scale)),
        )

    def size(self) -> dict[str, float]:
        bbox = self.get_bounding_box()
        return {
            "width": bbox.max.x - bbox.min.x,
            "height": bbox.max.y - bbox.min.y,
            "depth": bbox.max.z - bbox.min.z,
        }
