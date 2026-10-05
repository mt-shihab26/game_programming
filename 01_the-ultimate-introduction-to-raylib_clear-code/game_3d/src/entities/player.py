from pyray import WHITE, Model, Vector3, draw_model
from core.entity import Entity


class Player(Entity):
    def __init__(self, model: Model) -> None:
        self.position = Vector3(0, 0, 0)
        self.scale = 1
        self.model = model

    def draw(self) -> None:
        draw_model(self.model, self.position, self.scale, WHITE)
