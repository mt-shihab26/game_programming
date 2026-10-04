from math import cos, sin
from pyray import draw_text, get_mouse_delta, get_mouse_wheel_move
from pyray import get_world_to_screen, is_mouse_button_down

from pyray import Camera3D, CameraProjection, Color, MouseButton, Vector3
from core.entity import Entity
from core.vector import V, Vec


class Observer(Entity):
    """The outside view: drag to orbit, wheel to zoom."""

    def __init__(self) -> None:
        self.reset()
        self.camera = Camera3D()
        self.camera.target = Vector3(0, 1, 0)
        self.camera.up = Vector3(0, 1, 0)
        self.camera.fovy = 45.0
        self.camera.projection = CameraProjection.CAMERA_PERSPECTIVE

    def reset(self) -> None:
        self.yaw, self.pitch, self.dist = 0.7, 0.5, 24.0

    def update(self, delta_time: float) -> None:
        if is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT):
            delta = get_mouse_delta()
            self.yaw -= delta.x * 0.005
            self.pitch = max(-1.5, min(self.pitch + delta.y * 0.005, 1.5))
        self.dist = max(5, min(self.dist - get_mouse_wheel_move() * 1.5, 60))
        self.camera.position = Vector3(
            self.dist * cos(self.pitch) * sin(self.yaw),
            self.dist * sin(self.pitch) + 1,
            self.dist * cos(self.pitch) * cos(self.yaw),
        )

    def label(self, text: str, world_pos: Vec, color: Color) -> None:
        p = get_world_to_screen(V(world_pos), self.camera)
        draw_text(text, int(p.x) + 10, int(p.y) - 8, 18, color)
