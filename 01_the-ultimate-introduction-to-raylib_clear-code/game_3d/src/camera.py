from pyray import Camera3D, Vector3
from raylib import CAMERA_PERSPECTIVE


class Camera:
    def __init__(self) -> None:
        position = Vector3(0, 20, 20)
        target = Vector3(0, 0, 0)
        up = Vector3(0, 1, 0)
        fovy = 45

        self.object = Camera3D(
            position,
            target,
            up,
            fovy,
            CAMERA_PERSPECTIVE,
        )

    def update(self):
        pass
