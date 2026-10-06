from pyray import (
    RED,
    Vector3,
    gen_mesh_sphere,
    load_model_from_mesh,
    normalize,
    unload_model,
    draw_model,
    vector3_normalize,
)

from random import uniform
from core.entity import Entity


class Obstacle(Entity):
    def __init__(self) -> None:
        self.radius = 2
        self.rings = 10
        self.slices = 30

        self.mesh = gen_mesh_sphere(self.radius, self.rings, self.slices)
        self.model = load_model_from_mesh(self.mesh)

        self.position = Vector3(uniform(-10, 10), 0, -35)
        self.scale = 1.0
        self.direction = Vector3(uniform(-0.4, 0.4), 0, 1)
        self.speed = 10

    def close(self) -> None:
        unload_model(self.model)

    def update(self, dt: float) -> None:
        self.direction = vector3_normalize(self.direction)
        self.position.x += self.direction.x * self.speed * dt
        self.position.y += self.direction.y * self.speed * dt
        self.position.z += self.direction.z * self.speed * dt

    def draw(self) -> None:
        draw_model(self.model, self.position, self.scale, RED)
