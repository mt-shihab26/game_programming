from random import uniform
from pyray import gen_mesh_sphere, load_model_from_mesh, unload_model

from pyray import Vector3
from core.sprite import Sprite

from raylib import MATERIAL_MAP_ALBEDO
from pyray import RED


class Obstacle(Sprite):
    def __init__(self) -> None:
        self.radius = 2
        self.rings = 10
        self.slices = 30

        self.mesh = gen_mesh_sphere(self.radius, self.rings, self.slices)

        model = load_model_from_mesh(self.mesh)

        model.materials[0].maps[MATERIAL_MAP_ALBEDO].color = RED

        super().__init__(
            model=model,
            position=Vector3(uniform(-10, 10), 0, -35),
            direction=Vector3(uniform(-0.3, 0.3), 0, 1),
            speed=10,
        )

    def close(self) -> None:
        unload_model(self.model)
