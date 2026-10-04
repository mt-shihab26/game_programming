from pyray import draw_line_3d, draw_sphere

from core.entity import Entity
from core.vector import V

from pyray import MAROON


class Line(Entity):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.start = [-4.0, 0.0, -2.0]
        self.end = [5.0, 2.0, 3.0]

    def draw(self) -> None:
        draw_line_3d(V(self.start), V(self.end), MAROON)

    def draw_ends(self, active: str) -> None:
        # the end being moved is drawn bigger
        draw_sphere(V(self.start), 0.2 if active == "start" else 0.1, MAROON)
        draw_sphere(V(self.end), 0.2 if active == "end" else 0.1, MAROON)
