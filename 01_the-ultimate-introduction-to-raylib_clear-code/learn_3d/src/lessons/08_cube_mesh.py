from core.controls import axis

from pyray import KeyboardKey
from core.lesson import Lesson

from core.config import MESH_SPEED


class CubeMeshLesson(Lesson):
    title = "gen_mesh_cube(width, height, length)"
    lines = [
        "A mesh is a shape built from flat triangles.",
        "width is its size along X (red), height along Y (green),",
        "length along Z (blue).",
        "(1, 1, 1) is a cube. Change one number and it becomes a box.",
        "The mesh is built around its centre, so it grows both ways.",
    ]
    keys = "A/D: width    Q/E: height    W/S: length"
    highlights = ("gen_mesh_cube",)
    show_camera = False

    def update(self, delta_time: float) -> None:
        step = MESH_SPEED * delta_time
        self.scene.cube.reshape(
            axis(KeyboardKey.KEY_D, KeyboardKey.KEY_A) * step,
            axis(KeyboardKey.KEY_E, KeyboardKey.KEY_Q) * step,
            axis(KeyboardKey.KEY_W, KeyboardKey.KEY_S) * step,
        )
