from math import cos, radians, sin, sqrt, tan

from pyray import *
from raylib import (
    CAMERA_ORTHOGRAPHIC,
    CAMERA_PERSPECTIVE,
    KEY_A,
    KEY_C,
    KEY_D,
    KEY_E,
    KEY_LEFT,
    KEY_Q,
    KEY_R,
    KEY_RIGHT,
    KEY_S,
    KEY_SPACE,
    KEY_W,
    KEY_X,
    KEY_Z,
    MOUSE_BUTTON_LEFT,
)

WINDOW_W, WINDOW_H = 1280, 720
INSET_W, INSET_H = 416, 234
MOVE_KEYS = "A/D: x    Q/E: y    W/S: z"

LESSONS = [
    (
        "A point is three numbers",
        [
            "Every position in 3D is Vector3(x, y, z).",
            "X = right (red), Y = up (green), Z = toward you (blue).",
            "Follow the path: walk x along red, z along blue, then climb y.",
        ],
        MOVE_KEYS,
    ),
    (
        "camera.position",
        [
            "Where your eye is in the world.",
            "The black ball is the camera. The small picture is what it sees.",
            "Move it and watch both views change.",
        ],
        MOVE_KEYS,
    ),
    (
        "camera.target",
        [
            "The point the camera looks at (pink ball).",
            "The camera stays where it is and turns to face it.",
        ],
        MOVE_KEYS,
    ),
    (
        "camera.fovy",
        [
            "How wide the lens is, in degrees.",
            "The blue pyramid is everything the camera can see.",
            "Wider angle: you see more, so things look smaller.",
        ],
        "W/S: fovy",
    ),
    (
        "camera.projection",
        [
            "PERSPECTIVE: far things look smaller (a pyramid).",
            "ORTHOGRAPHIC: size never changes with distance (a box).",
            "In orthographic, fovy is the view height in world units.",
        ],
        "SPACE: switch    W/S: fovy",
    ),
    (
        "camera.up",
        [
            "Up does not move the camera or change where it looks.",
            "It only says which side of the picture is the top.",
            "The green stick on the camera is up. The green edge is the",
            "top of the picture. Lean the stick and the picture leans too,",
            "like tilting your head sideways.",
            "Only the direction counts: (0, 1, 0) and (0, 10, 0) are the same.",
        ],
        MOVE_KEYS,
    ),
    (
        "draw_model(model, position, scale, tint)",
        [
            "position places the centre of the cube.",
            "At y = 0 half the cube is under the floor. y = 0.5 sits on it.",
        ],
        MOVE_KEYS + "    Z/X: scale",
    ),
    (
        "draw_line_3d(start, end, color): start",
        [
            "A line is just two points joined together.",
            "This lesson moves the first point (start).",
            "y = 0 keeps that end on the floor. Raise y and it lifts up.",
        ],
        MOVE_KEYS,
    ),
    (
        "draw_line_3d(start, end, color): end",
        [
            "Now move the second point (end).",
            "The line always runs straight between the two points,",
            "so moving one end swings and stretches the whole line.",
        ],
        MOVE_KEYS,
    ),
]


def V(v):
    return Vector3(v[0], v[1], v[2])


def add(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]


def sub(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]


def scale(a, s):
    return [a[0] * s, a[1] * s, a[2] * s]


def cross(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]


def length(a):
    return sqrt(a[0] * a[0] + a[1] * a[1] + a[2] * a[2])


def norm(a):
    l = length(a)
    return scale(a, 1 / l) if l > 0.0001 else [0, 0, 0]


def fmt(v):
    return f"Vector3({v[0]:.1f}, {v[1]:.1f}, {v[2]:.1f})"


def move(v, dt, speed=4):
    speed = speed * dt
    v[0] += (is_key_down(KEY_D) - is_key_down(KEY_A)) * speed
    v[1] += (is_key_down(KEY_E) - is_key_down(KEY_Q)) * speed
    v[2] += (is_key_down(KEY_S) - is_key_down(KEY_W)) * speed


class Point:
    """Lesson 1: a single position, drawn with the path that builds it."""

    def __init__(self):
        self.reset()

    def reset(self):
        self.pos = [3.0, 2.0, 2.0]

    def draw(self):
        x, y, z = self.pos
        draw_line_3d(V([0, 0, 0]), V([x, 0, 0]), RED)
        draw_line_3d(V([x, 0, 0]), V([x, 0, z]), BLUE)
        draw_line_3d(V([x, 0, z]), V([x, y, z]), GREEN)
        draw_sphere(V(self.pos), 0.15, PURPLE)


class Cube:
    def __init__(self):
        self.model = load_model_from_mesh(gen_mesh_cube(1, 1, 1))
        self.reset()

    def reset(self):
        self.pos = [0.0, 0.0, 0.0]
        self.scale = 1.0

    def resize(self, amount):
        self.scale = max(0.1, min(self.scale + amount, 5))

    def draw(self):
        draw_model(self.model, V(self.pos), self.scale, ORANGE)
        draw_model_wires(self.model, V(self.pos), self.scale, DARKBROWN)


class Line:
    def __init__(self):
        self.reset()

    def reset(self):
        self.start = [-4.0, 0.0, -2.0]
        self.end = [5.0, 2.0, 3.0]

    def draw(self):
        draw_line_3d(V(self.start), V(self.end), MAROON)

    def draw_ends(self, active):
        # the end being moved is drawn bigger
        draw_sphere(V(self.start), 0.2 if active == "start" else 0.1, MAROON)
        draw_sphere(V(self.end), 0.2 if active == "end" else 0.1, MAROON)


class LessonCamera:
    """The camera being taught. Drawn in the world as a gizmo."""

    def __init__(self):
        self.camera = Camera3D()
        self.reset()

    def reset(self):
        self.pos = [0.0, 10.0, 5.0]
        self.target = [0.0, 0.0, 0.0]
        self.up = [0.0, 1.0, 0.0]
        self.fovy = 45.0
        self.projection = CAMERA_PERSPECTIVE
        self.picture_top = [0.0, 0.0, 0.0]

    @property
    def up_tip(self):
        return add(self.pos, scale(norm(self.up), 2))

    @property
    def projection_name(self):
        if self.projection == CAMERA_PERSPECTIVE:
            return "CAMERA_PERSPECTIVE"
        return "CAMERA_ORTHOGRAPHIC"

    def change_fovy(self, amount):
        self.fovy = max(1, min(self.fovy + amount, 120))

    def toggle_projection(self):
        if self.projection == CAMERA_PERSPECTIVE:
            self.projection, self.fovy = CAMERA_ORTHOGRAPHIC, 10.0
        else:
            self.projection, self.fovy = CAMERA_PERSPECTIVE, 45.0

    def update(self):
        self.camera.position = V(self.pos)
        self.camera.target = V(self.target)
        # a zero-length up has no direction, so fall back to the sky
        self.camera.up = V(self.up if length(self.up) > 0.01 else [0, 1, 0])
        self.camera.fovy = self.fovy
        self.camera.projection = self.projection

    def draw_gizmo(self):
        forward = norm(sub(self.target, self.pos))
        right = cross(forward, self.up)
        right = norm(right) if length(right) > 0.0001 else [1, 0, 0]
        up = cross(right, forward)

        depth = max(length(sub(self.target, self.pos)), 1)
        aspect = INSET_W / INSET_H
        if self.projection == CAMERA_PERSPECTIVE:
            half_h = depth * tan(radians(self.fovy) / 2)
        else:
            half_h = self.fovy / 2
        half_w = half_h * aspect

        far_center = add(self.pos, scale(forward, depth))
        far, near = [], []
        for sx, sy in ((-1, 1), (1, 1), (1, -1), (-1, -1)):
            offset = add(scale(right, sx * half_w), scale(up, sy * half_h))
            far.append(add(far_center, offset))
            if self.projection == CAMERA_PERSPECTIVE:
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
        draw_line_3d(V(self.pos), V(self.up_tip), LIME)
        draw_sphere(V(self.pos), 0.25, BLACK)
        draw_sphere(V(self.target), 0.15, PINK)


class Observer:
    """The outside view: drag to orbit, wheel to zoom."""

    def __init__(self):
        self.reset()
        self.camera = Camera3D()
        self.camera.target = Vector3(0, 1, 0)
        self.camera.up = Vector3(0, 1, 0)
        self.camera.fovy = 45.0
        self.camera.projection = CAMERA_PERSPECTIVE

    def reset(self):
        self.yaw, self.pitch, self.dist = 0.7, 0.5, 24.0

    def update(self):
        if is_mouse_button_down(MOUSE_BUTTON_LEFT):
            delta = get_mouse_delta()
            self.yaw -= delta.x * 0.005
            self.pitch = max(-1.5, min(self.pitch + delta.y * 0.005, 1.5))
        self.dist = max(5, min(self.dist - get_mouse_wheel_move() * 1.5, 60))
        self.camera.position = Vector3(
            self.dist * cos(self.pitch) * sin(self.yaw),
            self.dist * sin(self.pitch) + 1,
            self.dist * cos(self.pitch) * cos(self.yaw),
        )

    def label(self, text, world_pos, color):
        p = get_world_to_screen(V(world_pos), self.camera)
        draw_text(text, int(p.x) + 10, int(p.y) - 8, 18, color)


class App:
    def __init__(self):
        init_window(WINDOW_W, WINDOW_H, "Learn 3D")
        self.inset = load_render_texture(INSET_W, INSET_H)
        self.lesson = 0
        self.point = Point()
        self.cube = Cube()
        self.line = Line()
        self.cam = LessonCamera()
        self.observer = Observer()

    @property
    def show_camera(self):
        return self.lesson > 0

    @property
    def line_end(self):
        # which end of the line the current lesson moves, if any
        return {7: "start", 8: "end"}.get(self.lesson)

    def reset(self):
        self.point.reset()
        self.cube.reset()
        self.line.reset()
        self.cam.reset()

    def update(self, dt):
        if is_key_pressed(KEY_RIGHT):
            self.lesson = min(self.lesson + 1, len(LESSONS) - 1)
        if is_key_pressed(KEY_LEFT):
            self.lesson = max(self.lesson - 1, 0)
        if is_key_pressed(KEY_R):
            self.reset()
        if is_key_pressed(KEY_C):
            self.observer.reset()

        self.update_lesson(dt)
        self.cam.update()
        self.observer.update()

    def update_lesson(self, dt):
        if self.lesson == 0:
            move(self.point.pos, dt)
        elif self.lesson == 1:
            move(self.cam.pos, dt)
        elif self.lesson == 2:
            move(self.cam.target, dt)
        elif self.lesson in (3, 4):
            self.cam.change_fovy((is_key_down(KEY_W) - is_key_down(KEY_S)) * 30 * dt)
            if self.lesson == 4 and is_key_pressed(KEY_SPACE):
                self.cam.toggle_projection()
        elif self.lesson == 5:
            move(self.cam.up, dt, 1)
        elif self.lesson == 6:
            move(self.cube.pos, dt)
            self.cube.resize((is_key_down(KEY_X) - is_key_down(KEY_Z)) * 1.5 * dt)
        elif self.lesson == 7:
            move(self.line.start, dt)
        elif self.lesson == 8:
            move(self.line.end, dt)

    def draw_scene(self):
        draw_grid(10, 1)
        draw_line_3d(V([0, 0, 0]), V([6, 0, 0]), RED)
        draw_line_3d(V([0, 0, 0]), V([0, 6, 0]), GREEN)
        draw_line_3d(V([0, 0, 0]), V([0, 0, 6]), BLUE)
        draw_sphere(V([6, 0, 0]), 0.1, RED)
        draw_sphere(V([0, 6, 0]), 0.1, GREEN)
        draw_sphere(V([0, 0, 6]), 0.1, BLUE)
        self.cube.draw()
        self.line.draw()

    def render_inset(self):
        # what the taught camera sees
        begin_texture_mode(self.inset)
        clear_background(WHITE)
        begin_mode_3d(self.cam.camera)
        self.draw_scene()
        end_mode_3d()
        end_texture_mode()

    def draw_world(self):
        begin_mode_3d(self.observer.camera)
        self.draw_scene()
        if self.show_camera:
            self.cam.draw_gizmo()
        else:
            self.point.draw()
        if self.line_end:
            self.line.draw_ends(self.line_end)
        end_mode_3d()

    def draw_labels(self):
        label = self.observer.label
        label("X", [6, 0, 0], RED)
        label("Y", [0, 6, 0], DARKGREEN)
        label("Z", [0, 0, 6], BLUE)
        if self.show_camera:
            label("camera.position", self.cam.pos, BLACK)
            label("camera.target", self.cam.target, MAROON)
            label("up", self.cam.up_tip, DARKGREEN)
            label("top of picture", self.cam.picture_top, DARKGREEN)
        else:
            label(fmt(self.point.pos), self.point.pos, PURPLE)
        if self.line_end:
            label("start", self.line.start, MAROON)
            label("end", self.line.end, MAROON)

    def draw_lesson_text(self):
        title, lines, keys = LESSONS[self.lesson]
        draw_text(f"{self.lesson + 1}/{len(LESSONS)}  {title}", 20, 20, 30, BLACK)
        for i, line in enumerate(lines):
            draw_text(line, 20, 64 + i * 26, 20, DARKGRAY)
        draw_text(keys, 20, 76 + len(lines) * 26, 20, DARKBLUE)

    def draw_code(self):
        # live code: the line this lesson changes is highlighted
        cam, cube, line = self.cam, self.cube, self.line
        code = [
            (f"point = {fmt(self.point.pos)}", (0,)),
            (f"camera.position = {fmt(cam.pos)}", (1,)),
            (f"camera.target = {fmt(cam.target)}", (2,)),
            (f"camera.fovy = {cam.fovy:.1f}", (3, 4)),
            (f"camera.projection = {cam.projection_name}", (4,)),
            (f"camera.up = {fmt(cam.up)}", (5,)),
            (f"draw_model(model, {fmt(cube.pos)}, {cube.scale:.1f}, ORANGE)", (6,)),
            (f"draw_line_3d({fmt(line.start)}, {fmt(line.end)}, MAROON)", (7, 8)),
        ]
        screen_h = get_screen_height()
        code_y = screen_h - 60 - len(code) * 24
        for i, (text, lessons) in enumerate(code):
            active = self.lesson in lessons
            draw_text(text, 20, code_y + i * 24, 20, RED if active else GRAY)

        draw_text(
            "LEFT/RIGHT: lesson    drag mouse: look around    wheel: zoom    R: reset lesson values    C: reset view",
            20,
            screen_h - 30,
            18,
            DARKGRAY,
        )

    def draw_inset(self):
        x, y = get_screen_width() - INSET_W - 20, 44
        draw_text("What this camera sees", x, y - 24, 18, BLACK)
        draw_text("top", x + INSET_W - 34, y - 24, 18, DARKGREEN)
        draw_texture_rec(
            self.inset.texture,
            Rectangle(0, 0, INSET_W, -INSET_H),
            Vector2(x, y),
            WHITE,
        )
        draw_rectangle_lines(x - 1, y - 1, INSET_W + 2, INSET_H + 2, BLACK)
        draw_rectangle(x - 1, y - 4, INSET_W + 2, 4, LIME)

    def draw(self):
        if self.show_camera:
            self.render_inset()

        begin_drawing()
        clear_background(RAYWHITE)
        self.draw_world()
        self.draw_labels()
        self.draw_lesson_text()
        self.draw_code()
        if self.show_camera:
            self.draw_inset()
        end_drawing()

    def run(self):
        while not window_should_close():
            self.update(get_frame_time())
            self.draw()
        unload_render_texture(self.inset)
        close_window()


if __name__ == "__main__":
    App().run()
