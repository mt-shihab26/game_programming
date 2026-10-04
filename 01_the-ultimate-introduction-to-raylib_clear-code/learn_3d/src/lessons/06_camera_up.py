from core.controls import MOVE_KEYS, move

from core.lesson import Lesson

from core.config import UP_SPEED


class CameraUpLesson(Lesson):
    title = "camera.up"
    lines = [
        "Up does not move the camera or change where it looks.",
        "It only says which side of the picture is the top.",
        "The green stick on the camera is up. The green edge is the",
        "top of the picture. Lean the stick and the picture leans too,",
        "like tilting your head sideways.",
        "Only the direction counts: (0, 1, 0) and (0, 10, 0) are the same.",
    ]
    keys = MOVE_KEYS
    highlights = ("camera.up",)

    def update(self, delta_time: float) -> None:
        move(self.scene.cam.up, delta_time, UP_SPEED)
