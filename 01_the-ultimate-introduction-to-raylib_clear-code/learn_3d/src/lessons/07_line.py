from pyray import is_key_pressed
from core.controls import MOVE_KEYS, move

from pyray import KeyboardKey
from typing import TYPE_CHECKING
from core.lesson import Label, Lesson

from pyray import MAROON

if TYPE_CHECKING:
    from entities.scene import Scene


class LineLesson(Lesson):
    title = "draw_line_3d(start, end, color)"
    lines = [
        "A line is just two points joined together.",
        "The big ball is the point you are moving. SPACE picks the other one.",
        "y = 0 keeps that end on the floor. Raise y and it lifts up.",
        "The line always runs straight between the two points,",
        "so moving one end swings and stretches the whole line.",
    ]
    keys = MOVE_KEYS + "    SPACE: start/end"
    highlights = ("draw_line_3d",)

    def __init__(self, scene: "Scene") -> None:
        super().__init__(scene)
        self.active = "start"

    def update(self, delta_time: float) -> None:
        if is_key_pressed(KeyboardKey.KEY_SPACE):
            self.active = "end" if self.active == "start" else "start"
        line = self.scene.line
        move(line.start if self.active == "start" else line.end, delta_time)

    def draw(self) -> None:
        super().draw()
        self.scene.line.draw_ends(self.active)

    def draw_labels(self, label: Label) -> None:
        super().draw_labels(label)
        line = self.scene.line
        label("start", line.start, MAROON)
        label("end", line.end, MAROON)
