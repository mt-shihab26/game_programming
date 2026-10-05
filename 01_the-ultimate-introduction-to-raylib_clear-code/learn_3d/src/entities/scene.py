from pyray import draw_grid

from core.entity import Entity
from core.lesson import Lesson
from entities.axes import Axes
from entities.ball import Ball
from entities.cube import Cube
from entities.cylinder import Cylinder
from entities.lesson_camera import LessonCamera
from entities.line import Line
from entities.point import Point

from pyray import BLUE, GRAY


class Scene(Entity):
    """Everything the lessons teach about, shared by all of them."""

    def __init__(self) -> None:
        self.axes = Axes()
        self.point = Point()
        self.cube = Cube()
        self.cylinder = Cylinder()
        self.line = Line()
        self.cam = LessonCamera()
        # collisions: the player is moved into the obstacle
        self.player_ball = Ball([0.0, 0.0, 0.0], 0.5, BLUE)
        self.obstacle_ball = Ball([3.0, 0.0, 0.0], 2.0, GRAY)
        self.player_box = Cube(color=BLUE)
        self.obstacle_box = Cube([3.0, 0.0, 0.0], [2.0, 1.0, 4.0], GRAY)
        # name (matched against Lesson.objects) -> the object drawn
        self.objects: dict[str, Entity] = {
            "point": self.point,
            "cube": self.cube,
            "line": self.line,
            "cylinder": self.cylinder,
            "player_ball": self.player_ball,
            "obstacle_ball": self.obstacle_ball,
            "player_box": self.player_box,
            "obstacle_box": self.obstacle_box,
        }

    def reset(self) -> None:
        self.point.reset()
        self.cube.reset()
        self.cylinder.reset()
        self.line.reset()
        self.cam.reset()
        self.player_ball.reset()
        self.obstacle_ball.reset()
        self.player_box.reset()
        self.obstacle_box.reset()

    def close(self) -> None:
        self.cube.close()
        self.cylinder.close()
        self.player_ball.close()
        self.obstacle_ball.close()
        self.player_box.close()
        self.obstacle_box.close()

    def update(self, delta_time: float) -> None:
        self.cam.update(delta_time)

    def draw_for(self, lesson: Lesson) -> None:
        # only the floor and what the lesson is about
        draw_grid(10, 1)
        self.axes.draw()
        for name in lesson.objects:
            self.objects[name].draw()
