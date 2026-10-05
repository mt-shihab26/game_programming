from math import asin, atan2, cos, radians, sin

from pyray import (
    Camera3D,
    Vector3,
    clamp,
    get_mouse_delta,
    get_mouse_wheel_move,
    is_mouse_button_down,
    vector3_add,
    vector3_length,
    vector3_normalize,
    vector3_scale,
    vector3_subtract,
)
from raylib import CAMERA_PERSPECTIVE, MOUSE_BUTTON_LEFT

from entity import Entity


class Camera(Entity):
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
        self.orbit_speed = 0.005
        self.max_pitch = radians(89)

    def update(self, dt: float) -> None:
        self.zoom()
        self.orbit()

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

    def orbit(self) -> None:
        if not is_mouse_button_down(MOUSE_BUTTON_LEFT):
            return

        delta = get_mouse_delta()

        if delta.x == 0 and delta.y == 0:
            return

        offset = vector3_subtract(self.object.position, self.object.target)
        distance = vector3_length(offset)

        yaw = atan2(offset.x, offset.z)
        pitch = asin(offset.y / distance)

        yaw -= delta.x * self.orbit_speed
        pitch = clamp(
            pitch + delta.y * self.orbit_speed,
            -self.max_pitch,
            self.max_pitch,
        )

        offset = Vector3(
            distance * cos(pitch) * sin(yaw),
            distance * sin(pitch),
            distance * cos(pitch) * cos(yaw),
        )

        self.object.position = vector3_add(self.object.target, offset)
