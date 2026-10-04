from core.controls import MOVE_KEYS, move

from core.lesson import Label, Lesson

from pyray import MAROON


class LineStartLesson(Lesson):
    title = "draw_line_3d(start, end, color): start"
    lines = [
        "A line is just two points joined together.",
        "This lesson moves the first point (start).",
        "y = 0 keeps that end on the floor. Raise y and it lifts up.",
    ]
    keys = MOVE_KEYS
    highlights = ("draw_line_3d",)

    def update(self, delta_time: float) -> None:
        move(self.scene.line.start, delta_time)

    def draw(self) -> None:
        super().draw()
        self.scene.line.draw_ends("start")

    def draw_labels(self, label: Label) -> None:
        super().draw_labels(label)
        line = self.scene.line
        label("start", line.start, MAROON)
        label("end", line.end, MAROON)
