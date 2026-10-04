from pyray import draw_model, draw_model_wires, gen_mesh_cylinder
from pyray import load_model_from_mesh, unload_model

from pyray import Model
from core.entity import Entity
from core.vector import V

from pyray import MAROON, RED


class Cylinder(Entity):
    def __init__(self) -> None:
        self.pos = [0.0, 0.0, 0.0]
        self.set_defaults()
        self.model = self.build()

    def set_defaults(self) -> None:
        self.radius = 1.0
        self.height = 2.0
        self.slices = 10

    def build(self) -> Model:
        mesh = gen_mesh_cylinder(self.radius, self.height, self.slices)
        return load_model_from_mesh(mesh)

    def rebuild(self) -> None:
        # the shape is baked into the mesh, so new numbers need a new mesh
        unload_model(self.model)
        self.model = self.build()

    def reset(self) -> None:
        self.set_defaults()
        self.rebuild()

    def resize(self, radius: float, height: float, slices: int) -> None:
        if not (radius or height or slices):
            return
        self.radius = max(0.1, min(self.radius + radius, 3))
        self.height = max(0.1, min(self.height + height, 6))
        self.slices = max(3, min(self.slices + slices, 50))
        self.rebuild()

    def close(self) -> None:
        unload_model(self.model)

    def draw(self) -> None:
        draw_model(self.model, V(self.pos), 1, RED)
        draw_model_wires(self.model, V(self.pos), 1, MAROON)
