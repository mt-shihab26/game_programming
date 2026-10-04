from core.controls import axis

from pyray import KeyboardKey
from core.lesson import Lesson

from core.config import FOVY_SPEED


class CameraFovyLesson(Lesson):
    title = "camera.fovy"
    lines = [
        "How wide the lens is, in degrees.",
        "The blue pyramid is everything the camera can see.",
        "Wider angle: you see more, so things look smaller.",
    ]
    keys = "W/S: fovy"
    code = ("camera.fovy",)
    objects = ("cube",)
    show_camera = True

    def update(self, delta_time: float) -> None:
        amount = axis(KeyboardKey.KEY_W, KeyboardKey.KEY_S)
        self.scene.cam.change_fovy(amount * FOVY_SPEED * delta_time)
