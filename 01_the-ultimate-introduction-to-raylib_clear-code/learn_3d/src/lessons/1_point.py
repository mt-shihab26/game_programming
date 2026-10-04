from core.controls import MOVE_KEYS, move

from core.lesson import Label, Lesson
from core.vector import fmt

from pyray import PURPLE


class PointLesson(Lesson):
    title = "A point is three numbers"
    lines = [
        "Every position in 3D is Vector3(x, y, z).",
        "X = right (red), Y = up (green), Z = toward you (blue).",
        "Follow the path: walk x along red, z along blue, then climb y.",
    ]
    keys = MOVE_KEYS
    highlights = ("point",)
    show_camera = False

    def update(self, delta_time: float) -> None:
        move(self.scene.point.pos, delta_time)

    def draw(self) -> None:
        self.scene.point.draw()

    def draw_labels(self, label: Label) -> None:
        point = self.scene.point
        label(fmt(point.pos), point.pos, PURPLE)
