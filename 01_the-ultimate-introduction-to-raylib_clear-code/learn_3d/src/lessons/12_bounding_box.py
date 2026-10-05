from pyray import draw_bounding_box, draw_sphere
from core.controls import MOVE_KEYS, move

from core.lesson import Label, Lesson
from core.vector import fmt, vec

from pyray import DARKGREEN, GREEN


class BoundingBoxLesson(Lesson):
    title = "BoundingBox(min, max)"
    lines = [
        "The smallest box that holds the whole mesh (green).",
        "It is only two corners: min has the lowest x, y and z,",
        "max has the highest.",
        "get_mesh_bounding_box gives them around (0, 0, 0), where the mesh",
        "was built. Add the position to both and the box follows the model.",
    ]
    keys = MOVE_KEYS
    code = ("player_box.position", "bounding_box.min", "bounding_box.max")
    objects = ("player_box",)

    def update(self, delta_time: float) -> None:
        move(self.scene.player_box.pos, delta_time)

    def draw(self) -> None:
        super().draw()
        box = self.scene.player_box.bounding_box()
        draw_bounding_box(box, GREEN)
        draw_sphere(box.min, 0.08, DARKGREEN)
        draw_sphere(box.max, 0.08, DARKGREEN)

    def draw_labels(self, label: Label) -> None:
        super().draw_labels(label)
        box = self.scene.player_box.bounding_box()
        low, high = vec(box.min), vec(box.max)
        label(f"min {fmt(low)}", low, DARKGREEN)
        label(f"max {fmt(high)}", high, DARKGREEN)
