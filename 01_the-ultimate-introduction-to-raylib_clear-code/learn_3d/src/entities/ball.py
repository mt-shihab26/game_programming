from pyray import check_collision_spheres, draw_model_wires, gen_mesh_sphere
from pyray import load_model_from_mesh, unload_model

from pyray import Color
from core.entity import Entity
from core.vector import V, Vec

from pyray import RED


class Ball(Entity):
    def __init__(self, home: Vec, radius: float, color: Color) -> None:
        self.home = home
        self.radius = radius
        self.color = color
        # set by the lesson: a ball that is hit is drawn red
        self.hit = False
        self.model = load_model_from_mesh(gen_mesh_sphere(radius, 12, 12))
        self.reset()

    def reset(self) -> None:
        self.pos = list(self.home)

    def hits(self, other: "Ball") -> bool:
        return check_collision_spheres(
            V(self.pos), self.radius, V(other.pos), other.radius
        )

    def close(self) -> None:
        unload_model(self.model)

    def draw(self) -> None:
        draw_model_wires(self.model, V(self.pos), 1, RED if self.hit else self.color)
