from pyray import draw_line_3d, draw_sphere

from core.entity import Entity
from core.vector import V

from pyray import BLUE, GREEN, RED

AXIS_LENGTH = 6


class Axes(Entity):
    def __init__(self) -> None:
        self.x = [AXIS_LENGTH, 0, 0]
        self.y = [0, AXIS_LENGTH, 0]
        self.z = [0, 0, AXIS_LENGTH]

    def draw(self) -> None:
        for tip, color in ((self.x, RED), (self.y, GREEN), (self.z, BLUE)):
            draw_line_3d(V([0, 0, 0]), V(tip), color)
            draw_sphere(V(tip), 0.1, color)
