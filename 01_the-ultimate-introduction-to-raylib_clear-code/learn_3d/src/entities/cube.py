from pyray import draw_model_wires, gen_mesh_cube
from pyray import load_model_from_mesh, unload_model

from pyray import Model
from core.entity import Entity
from core.vector import V

from pyray import ORANGE


class Cube(Entity):
    def __init__(self) -> None:
        self.set_defaults()
        self.model = self.build()

    def set_defaults(self) -> None:
        self.pos = [0.0, 0.0, 0.0]
        self.scale = 1.0
        self.size = [1.0, 1.0, 1.0]

    def build(self) -> Model:
        return load_model_from_mesh(gen_mesh_cube(*self.size))

    def rebuild(self) -> None:
        # the shape is baked into the mesh, so new numbers need a new mesh
        unload_model(self.model)
        self.model = self.build()

    def reset(self) -> None:
        self.set_defaults()
        self.rebuild()

    def resize(self, amount: float) -> None:
        self.scale = max(0.1, min(self.scale + amount, 5))

    def reshape(self, width: float, height: float, length: float) -> None:
        if not (width or height or length):
            return
        for i, amount in enumerate((width, height, length)):
            self.size[i] = max(0.1, min(self.size[i] + amount, 5))
        self.rebuild()

    def close(self) -> None:
        unload_model(self.model)

    def draw(self) -> None:
        draw_model_wires(self.model, V(self.pos), self.scale, ORANGE)
