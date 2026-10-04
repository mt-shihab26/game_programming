from pyray import draw_text, get_screen_height

from core.vector import fmt
from entities.cube import Cube
from entities.lesson_camera import LessonCamera
from entities.line import Line
from entities.point import Point

from pyray import DARKGRAY, GRAY, RED

HINT = "LEFT/RIGHT: lesson    drag mouse: look around    wheel: zoom    R: reset lesson values    C: reset view"


class CodePanel:
    """Live code: the line the current lesson changes is highlighted."""

    def __init__(self, point: Point, cam: LessonCamera, cube: Cube, line: Line) -> None:
        self.point = point
        self.cam = cam
        self.cube = cube
        self.line = line

    def code(self) -> list[tuple[str, tuple[int, ...]]]:
        point, cam, cube, line = self.point, self.cam, self.cube, self.line
        return [
            (f"point = {fmt(point.pos)}", (0,)),
            (f"camera.position = {fmt(cam.pos)}", (1,)),
            (f"camera.target = {fmt(cam.target)}", (2,)),
            (f"camera.fovy = {cam.fovy:.1f}", (3, 4)),
            (f"camera.projection = {cam.projection_name()}", (4,)),
            (f"camera.up = {fmt(cam.up)}", (5,)),
            (f"draw_model(model, {fmt(cube.pos)}, {cube.scale:.1f}, ORANGE)", (6,)),
            (f"draw_line_3d({fmt(line.start)}, {fmt(line.end)}, MAROON)", (7, 8)),
        ]

    def draw(self, lesson: int) -> None:
        code = self.code()
        screen_h = get_screen_height()
        code_y = screen_h - 60 - len(code) * 24
        for i, (text, lessons) in enumerate(code):
            draw_text(text, 20, code_y + i * 24, 20, RED if lesson in lessons else GRAY)
        draw_text(HINT, 20, screen_h - 30, 18, DARKGRAY)
