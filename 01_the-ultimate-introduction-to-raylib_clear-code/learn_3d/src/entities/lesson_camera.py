from math import radians, tan
from pyray import draw_line_3d, draw_sphere

from pyray import Camera3D, CameraProjection
from core.entity import Entity
from core.vector import V, Vec, add, cross, length, norm, scale, sub

from pyray import BLACK, DARKGRAY, LIME, PINK, SKYBLUE
from core.config import INSET_HEIGHT, INSET_WIDTH

PERSPECTIVE = CameraProjection.CAMERA_PERSPECTIVE
ORTHOGRAPHIC = CameraProjection.CAMERA_ORTHOGRAPHIC


class LessonCamera(Entity):
    """The camera being taught. Drawn in the world as a gizmo."""

    def __init__(self) -> None:
        self.camera = Camera3D()
        self.reset()

    def reset(self) -> None:
        self.pos = [0.0, 10.0, 5.0]
        self.target = [0.0, 0.0, 0.0]
        self.up = [0.0, 1.0, 0.0]
        self.fovy = 45.0
        self.projection = PERSPECTIVE
        self.picture_top = [0.0, 0.0, 0.0]

    def up_tip(self) -> Vec:
        return add(self.pos, scale(norm(self.up), 2))

    def projection_name(self) -> str:
        if self.projection == PERSPECTIVE:
            return "CAMERA_PERSPECTIVE"
        return "CAMERA_ORTHOGRAPHIC"

    def change_fovy(self, amount: float) -> None:
        self.fovy = max(1, min(self.fovy + amount, 120))

    def toggle_projection(self) -> None:
        if self.projection == PERSPECTIVE:
            self.projection, self.fovy = ORTHOGRAPHIC, 10.0
        else:
            self.projection, self.fovy = PERSPECTIVE, 45.0

    def update(self, delta_time: float) -> None:
        self.camera.position = V(self.pos)
        self.camera.target = V(self.target)
        # a zero-length up has no direction, so fall back to the sky
        self.camera.up = V(self.up if length(self.up) > 0.01 else [0, 1, 0])
        self.camera.fovy = self.fovy
        self.camera.projection = self.projection

    def draw(self) -> None:
        forward = norm(sub(self.target, self.pos))
        right = cross(forward, self.up)
        right = norm(right) if length(right) > 0.0001 else [1, 0, 0]
        up = cross(right, forward)

        depth = max(length(sub(self.target, self.pos)), 1)
        if self.projection == PERSPECTIVE:
            half_h = depth * tan(radians(self.fovy) / 2)
        else:
            half_h = self.fovy / 2
        half_w = half_h * INSET_WIDTH / INSET_HEIGHT

        far_center = add(self.pos, scale(forward, depth))
        far, near = [], []
        for sx, sy in ((-1, 1), (1, 1), (1, -1), (-1, -1)):
            offset = add(scale(right, sx * half_w), scale(up, sy * half_h))
            far.append(add(far_center, offset))
            if self.projection == PERSPECTIVE:
                near.append(self.pos)
            else:
                near.append(add(self.pos, offset))

        for i in range(4):
            draw_line_3d(V(near[i]), V(far[i]), SKYBLUE)
            # far[0] -> far[1] is the top edge of the picture
            draw_line_3d(V(far[i]), V(far[(i + 1) % 4]), LIME if i == 0 else SKYBLUE)
            draw_line_3d(V(near[i]), V(near[(i + 1) % 4]), SKYBLUE)
        self.picture_top = scale(add(far[0], far[1]), 0.5)

        draw_line_3d(V(self.pos), V(self.target), DARKGRAY)
        draw_line_3d(V(self.pos), V(self.up_tip()), LIME)
        draw_sphere(V(self.pos), 0.25, BLACK)
        draw_sphere(V(self.target), 0.15, PINK)
