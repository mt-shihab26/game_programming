from pyray import Camera3D, Vector3
from raylib import CAMERA_PERSPECTIVE


class Camera:
    def __init__(self) -> None:
        self.position = Vector3(0, 10, 0)
        self.target = Vector3(0, 0, 0)
        self.up = Vector3(0, 0, -1)
        self.fovy = 45
        self.object = Camera3D(
            self.position,
            self.target,
            self.up,
            self.fovy,
            CAMERA_PERSPECTIVE,
        )
