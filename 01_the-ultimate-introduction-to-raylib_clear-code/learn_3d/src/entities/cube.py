from pyray import draw_model, draw_model_wires, gen_mesh_cube
from pyray import load_model_from_mesh, unload_model

from core.entity import Entity
from core.vector import V

from pyray import DARKBROWN, ORANGE


class Cube(Entity):
    def __init__(self) -> None:
        self.model = load_model_from_mesh(gen_mesh_cube(1, 1, 1))
        self.reset()

    def reset(self) -> None:
        self.pos = [0.0, 0.0, 0.0]
        self.scale = 1.0

    def resize(self, amount: float) -> None:
        self.scale = max(0.1, min(self.scale + amount, 5))

    def close(self) -> None:
        unload_model(self.model)

    def draw(self) -> None:
        draw_model(self.model, V(self.pos), self.scale, ORANGE)
        draw_model_wires(self.model, V(self.pos), self.scale, DARKBROWN)
