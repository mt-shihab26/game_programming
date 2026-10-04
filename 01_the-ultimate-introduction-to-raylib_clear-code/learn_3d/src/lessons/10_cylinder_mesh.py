from pyray import is_key_pressed
from core.controls import axis

from pyray import KeyboardKey
from core.lesson import Lesson

from core.config import MESH_SPEED


class CylinderMeshLesson(Lesson):
    title = "gen_mesh_cylinder(radius, height, slices)"
    lines = [
        "A mesh is a shape built from flat triangles.",
        "radius is how wide it is, height is how tall.",
        "slices is how many flat sides go around it.",
        "4 slices is a square pillar. 50 slices looks round.",
        "The bottom sits at y = 0, not the centre like the cube.",
    ]
    keys = "A/D: radius    W/S: height    Z/X: slices"
    code = ("gen_mesh_cylinder",)
    objects = ("cylinder",)

    def update(self, delta_time: float) -> None:
        radius = axis(KeyboardKey.KEY_D, KeyboardKey.KEY_A)
        height = axis(KeyboardKey.KEY_W, KeyboardKey.KEY_S)
        slices = is_key_pressed(KeyboardKey.KEY_X) - is_key_pressed(KeyboardKey.KEY_Z)
        self.scene.cylinder.resize(
            radius * MESH_SPEED * delta_time, height * MESH_SPEED * delta_time, slices
        )
