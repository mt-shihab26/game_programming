from pyray import (
    RED,
    Vector3,
    gen_mesh_sphere,
    load_model_from_mesh,
    unload_model,
    draw_model,
)

from core.entity import Entity


class Obstacle(Entity):
    def __init__(self) -> None:
        self.radius = 2
        self.rings = 10
        self.slices = 12

        self.mesh = gen_mesh_sphere(self.radius, self.rings, self.slices)
        self.model = load_model_from_mesh(self.mesh)

        self.position = Vector3(0, 0, 0)

    def close(self) -> None:
        unload_model(self.model)

    def draw(self) -> None:
        draw_model(self.model, self.position, 1.0, RED)
