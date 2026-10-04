from core.controls import MOVE_KEYS, move

from core.lesson import Lesson


class CameraPositionLesson(Lesson):
    title = "camera.position"
    lines = [
        "Where your eye is in the world.",
        "The black ball is the camera. The small picture is what it sees.",
        "Move it and watch both views change.",
    ]
    keys = MOVE_KEYS
    highlights = ("camera.position",)

    def update(self, delta_time: float) -> None:
        move(self.scene.cam.pos, delta_time)
