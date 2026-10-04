from pyray import draw_line_3d, draw_sphere

from core.entity import Entity
from core.vector import V

from pyray import BLUE, GREEN, PURPLE, RED


class Point(Entity):
    """Lesson 1: a single position, drawn with the path that builds it."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.pos = [3.0, 2.0, 2.0]

    def draw(self) -> None:
        x, y, z = self.pos
        draw_line_3d(V([0, 0, 0]), V([x, 0, 0]), RED)
        draw_line_3d(V([x, 0, 0]), V([x, 0, z]), BLUE)
        draw_line_3d(V([x, 0, z]), V([x, y, z]), GREEN)
        draw_sphere(V(self.pos), 0.15, PURPLE)
