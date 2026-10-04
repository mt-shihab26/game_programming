from pyray import is_key_pressed
from core.controls import axis

from pyray import KeyboardKey
from core.lesson import Lesson

from core.config import FOVY_SPEED


class CameraProjectionLesson(Lesson):
    title = "camera.projection"
    lines = [
        "PERSPECTIVE: far things look smaller (a pyramid).",
        "ORTHOGRAPHIC: size never changes with distance (a box).",
        "In orthographic, fovy is the view height in world units.",
    ]
    keys = "SPACE: switch    W/S: fovy"
    code = ("camera.fovy", "camera.projection")
    objects = ("cube",)
    show_camera = True

    def update(self, delta_time: float) -> None:
        cam = self.scene.cam
        amount = axis(KeyboardKey.KEY_W, KeyboardKey.KEY_S)
        cam.change_fovy(amount * FOVY_SPEED * delta_time)
        if is_key_pressed(KeyboardKey.KEY_SPACE):
            cam.toggle_projection()
