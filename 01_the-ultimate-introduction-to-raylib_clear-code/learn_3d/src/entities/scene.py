from pyray import draw_grid

from core.entity import Entity
from core.lesson import Lesson
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
        # name (matched against Lesson.objects) -> the object drawn
        self.objects: dict[str, Entity] = {
            "point": self.point,
            "cube": self.cube,
            "line": self.line,
            "cylinder": self.cylinder,
        }

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

    def draw_for(self, lesson: Lesson) -> None:
        # only the floor and what the lesson is about
        draw_grid(10, 1)
        self.axes.draw()
        for name in lesson.objects:
            self.objects[name].draw()
