from core.controls import MOVE_KEYS, move

from core.lesson import Lesson


class CameraTargetLesson(Lesson):
    title = "camera.target"
    lines = [
        "The point the camera looks at (pink ball).",
        "The camera stays where it is and turns to face it.",
    ]
    keys = MOVE_KEYS
    code = ("camera.target",)
    objects = ("cube",)
    show_camera = True

    def update(self, delta_time: float) -> None:
        move(self.scene.cam.target, delta_time)
