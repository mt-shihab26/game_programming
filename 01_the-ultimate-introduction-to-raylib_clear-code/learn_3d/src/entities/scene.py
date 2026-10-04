from pyray import draw_grid

from core.entity import Entity
from entities.axes import Axes
from entities.cube import Cube
from entities.cylinder import Cylinder
from entities.lesson_camera import LessonCamera
from entities.line import Line
from entities.point import Point


class Scene(Entity):
    """Everything the lessons teach about, shared by all of them."""

    def __init__(self) -> None:
        self.axes = Axes()
        self.point = Point()
        self.cube = Cube()
        self.cylinder = Cylinder()
        self.line = Line()
        self.cam = LessonCamera()

    def reset(self) -> None:
        self.point.reset()
        self.cube.reset()
        self.cylinder.reset()
        self.line.reset()
        self.cam.reset()

    def close(self) -> None:
        self.cube.close()
        self.cylinder.close()

    def update(self, delta_time: float) -> None:
        self.cam.update(delta_time)

    def draw(self) -> None:
        draw_grid(10, 1)
        self.axes.draw()
        self.cube.draw()
        self.line.draw()
