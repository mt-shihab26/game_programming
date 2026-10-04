from core.controls import MOVE_KEYS, move

from core.lesson import Label, Lesson

from pyray import MAROON


class LineEndLesson(Lesson):
    title = "draw_line_3d(start, end, color): end"
    lines = [
        "Now move the second point (end).",
        "The line always runs straight between the two points,",
        "so moving one end swings and stretches the whole line.",
    ]
    keys = MOVE_KEYS
    highlights = ("draw_line_3d",)

    def update(self, delta_time: float) -> None:
        move(self.scene.line.end, delta_time)

    def draw(self) -> None:
        super().draw()
        self.scene.line.draw_ends("end")

    def draw_labels(self, label: Label) -> None:
        super().draw_labels(label)
        line = self.scene.line
        label("start", line.start, MAROON)
        label("end", line.end, MAROON)
