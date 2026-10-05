from pyray import (
    Camera3D,
    Vector3,
    clamp,
    get_mouse_wheel_move,
    vector3_add,
    vector3_length,
    vector3_normalize,
    vector3_scale,
    vector3_subtract,
)
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
        self.zoom_speed = 2
        self.min_distance = 2
        self.max_distance = 50

    def update(self, dt: float) -> None:
        self.zoom()

    def zoom(self) -> None:
        wheel = get_mouse_wheel_move()

        if wheel == 0:
            return

        offset = vector3_subtract(self.object.position, self.object.target)
        distance = vector3_length(offset)
        direction = vector3_normalize(offset)

        distance = clamp(
            distance - wheel * self.zoom_speed,
            self.min_distance,
            self.max_distance,
        )

        self.object.position = vector3_add(
            self.object.target, vector3_scale(direction, distance)
        )
