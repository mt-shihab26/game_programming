from pyray import get_screen_height

from core.font import draw_text
from core.lesson import Lesson
from core.vector import fmt
from entities.scene import Scene

from pyray import DARKGRAY, RED

HINT = "LEFT/RIGHT: lesson    drag mouse: look around    wheel: zoom    R: reset lesson values    C: reset view"


class CodePanel:
    """Live code: the lines the current lesson is about."""

    def __init__(self, scene: Scene) -> None:
        self.scene = scene

    def code(self) -> dict[str, str]:
        # name (matched against Lesson.code) -> the code line shown
        point, cam = self.scene.point, self.scene.cam
        cube, line = self.scene.cube, self.scene.line
        cylinder = self.scene.cylinder
        return {
            "point": f"point = {fmt(point.pos)}",
            "camera.position": f"camera.position = {fmt(cam.pos)}",
            "camera.target": f"camera.target = {fmt(cam.target)}",
            "camera.fovy": f"camera.fovy = {cam.fovy:.1f}",
            "camera.projection": f"camera.projection = {cam.projection_name()}",
            "camera.up": f"camera.up = {fmt(cam.up)}",
            "draw_line_3d": f"draw_line_3d({fmt(line.start)}, {fmt(line.end)}, MAROON)",
            "gen_mesh_cube": f"mesh = gen_mesh_cube({cube.size[0]:.1f}, {cube.size[1]:.1f}, {cube.size[2]:.1f})",
            "draw_model_wires": f"draw_model_wires(model, {fmt(cube.pos)}, {cube.scale:.1f}, ORANGE)",
            "gen_mesh_cylinder": f"cylinder_mesh = gen_mesh_cylinder({cylinder.radius:.1f}, {cylinder.height:.1f}, {cylinder.slices})",
        }

    def draw(self, lesson: Lesson) -> None:
        code = self.code()
        screen_h = get_screen_height()
        code_y = screen_h - 60 - len(lesson.code) * 24
        for i, name in enumerate(lesson.code):
            draw_text(code[name], 20, code_y + i * 24, 20, RED)
        draw_text(HINT, 20, screen_h - 30, 18, DARKGRAY)
