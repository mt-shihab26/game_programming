from pyray import get_screen_height

from core.font import draw_text
from core.lesson import Lesson
from core.vector import fmt, vec
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
        player_ball, obstacle_ball = self.scene.player_ball, self.scene.obstacle_ball
        player_box, obstacle_box = self.scene.player_box, self.scene.obstacle_box
        box = player_box.bounding_box()
        overlap = player_box.overlap(obstacle_box)
        textured = self.scene.textured_cylinder
        return {
            **{
                f"overlap_{name}": f"overlap_{name} = ({obstacle_box.size[i]:.1f} / 2 + {player_box.size[i]:.1f} / 2) - abs({player_box.pos[i]:.1f} - {obstacle_box.pos[i]:.1f})  # {overlap[i]:.1f}"
                for i, name in enumerate("xyz")
            },
            "collision_axis": self.collision_axis(),
            "push_out": self.push_out(),
            "gen_image_gradient_linear": f"image = gen_image_gradient_linear(100, 100, {textured.direction}, RED, YELLOW)",
            "set_material_texture": "set_material_texture(model.materials[0], MATERIAL_MAP_ALBEDO, texture)",
            "load_shader": 'shader = load_shader(ffi.NULL, join("shaders", "grayscale.fs"))',
            "material.shader": "model.materials[0].shader = shader"
            if textured.gray
            else "# model.materials[0].shader = shader    off: raylib's own shader draws it",
            "grayscale.fs": "finalColor = vec4(gray, gray, gray, texelColor.a);    // grayscale.fs",
            "get_shader_location": f'flash_location = get_shader_location(shader, "flash")  # {textured.flash_location}',
            "flash_amount": f'flash_amount = ffi.new("struct Vector2*", [{textured.flash:.1f}, 0])',
            "set_shader_value": "set_shader_value(shader, flash_location, flash_amount, SHADER_UNIFORM_VEC2)",
            "flash.fs": f"finalColor = mix(texelColor, white, {textured.flash:.1f});    // flash.fs, where {textured.flash:.1f} is flash.x",
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
            "player_ball.position": f"player_position = {fmt(player_ball.pos)}",
            "obstacle_ball.position": f"obstacle_position = {fmt(obstacle_ball.pos)}",
            "player_box.position": f"player_position = {fmt(player_box.pos)}",
            "obstacle_box.position": f"obstacle_position = {fmt(obstacle_box.pos)}",
            "check_collision_spheres": f"check_collision_spheres(player_position, {player_ball.radius:.1f}, obstacle_position, {obstacle_ball.radius:.1f})  # {player_ball.hits(obstacle_ball)}",
            "bounding_box.min": f"min_boundary = vector3_add(player_position, bounding_box.min)  # {fmt(vec(box.min))}",
            "bounding_box.max": f"max_boundary = vector3_add(player_position, bounding_box.max)  # {fmt(vec(box.max))}",
            "check_collision_box_sphere": f"check_collision_box_sphere(player_bounding_box, obstacle_position, {obstacle_ball.radius:.1f})  # {player_box.hits_ball(obstacle_ball)}",
            "check_collision_boxes": f"check_collision_boxes(player_bounding_box, obstacle_bounding_box)  # {player_box.hits(obstacle_box)}",
        }

    def collision_axis(self) -> str:
        axis = self.scene.collision_axis
        return f'collision_axis = "{"" if axis is None else "xyz"[axis]}"'

    def push_out(self) -> str:
        axis = self.scene.collision_axis
        if axis is None:
            return "# not touching, so there is nothing to push out"
        player, obstacle = self.scene.player_box, self.scene.obstacle_box
        sign = "-" if player.pos[axis] < obstacle.pos[axis] else "+"
        return (
            f"player_position.{'xyz'[axis]} = {obstacle.pos[axis]:.1f}"
            f" {sign} {obstacle.size[axis]:.1f} / 2 {sign} {player.size[axis]:.1f} / 2"
            f"  # {player.pushed_out(obstacle, axis):.1f}"
        )

    def draw(self, lesson: Lesson) -> None:
        code = self.code()
        screen_h = get_screen_height()
        code_y = screen_h - 60 - len(lesson.code) * 24
        for i, name in enumerate(lesson.code):
            draw_text(code[name], 20, code_y + i * 24, 20, RED)
        draw_text(HINT, 20, screen_h - 30, 18, DARKGRAY)
