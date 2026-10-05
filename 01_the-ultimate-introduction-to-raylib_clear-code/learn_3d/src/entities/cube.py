from pyray import check_collision_box_sphere, check_collision_boxes
from pyray import draw_model_wires, gen_mesh_cube, get_mesh_bounding_box
from pyray import load_model_from_mesh, unload_model, vector3_add, vector3_scale

from pyray import BoundingBox, Color, Model
from typing import TYPE_CHECKING, Sequence
from core.entity import Entity
from core.vector import V, Vec

from pyray import ORANGE, RED

if TYPE_CHECKING:
    from entities.ball import Ball


class Cube(Entity):
    def __init__(
        self,
        home: Sequence[float] = (0.0, 0.0, 0.0),
        size: Sequence[float] = (1.0, 1.0, 1.0),
        color: Color = ORANGE,
    ) -> None:
        self.home = home
        self.home_size = size
        self.color = color
        # set by the lesson: a cube that is hit is drawn red
        self.hit = False
        self.set_defaults()
        self.model = self.build()

    def set_defaults(self) -> None:
        self.pos = list(self.home)
        self.scale = 1.0
        self.size = list(self.home_size)

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

    def bounding_box(self) -> BoundingBox:
        # the mesh's box sits around (0, 0, 0), so carry it to where the model is drawn
        box = get_mesh_bounding_box(self.model.meshes[0])
        position = V(self.pos)
        return BoundingBox(
            vector3_add(position, vector3_scale(box.min, self.scale)),
            vector3_add(position, vector3_scale(box.max, self.scale)),
        )

    def hits(self, other: "Cube") -> bool:
        return check_collision_boxes(self.bounding_box(), other.bounding_box())

    def hits_ball(self, ball: "Ball") -> bool:
        return check_collision_box_sphere(self.bounding_box(), V(ball.pos), ball.radius)

    def half(self, axis: int) -> float:
        return self.size[axis] * self.scale / 2

    def overlap(self, other: "Cube") -> Vec:
        # how deep the two boxes sit inside each other on x, y and z
        return [
            self.half(axis) + other.half(axis) - abs(self.pos[axis] - other.pos[axis])
            for axis in range(3)
        ]

    def push_axis(self, other: "Cube") -> int | None:
        # the axis with the smallest overlap is the one the cube came in on
        if not self.hits(other):
            return None
        overlap = self.overlap(other)
        return overlap.index(min(overlap))

    def pushed_out(self, other: "Cube", axis: int) -> float:
        # where this cube sits on that axis when the two only just touch
        reach = self.half(axis) + other.half(axis)
        side = -1 if self.pos[axis] < other.pos[axis] else 1
        return other.pos[axis] + side * reach

    def close(self) -> None:
        unload_model(self.model)

    def draw(self) -> None:
        color = RED if self.hit else self.color
        draw_model_wires(self.model, V(self.pos), self.scale, color)
