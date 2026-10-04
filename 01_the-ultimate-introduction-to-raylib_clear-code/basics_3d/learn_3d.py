from math import cos, radians, sin, sqrt, tan

from pyray import *
from raylib import (
    CAMERA_ORTHOGRAPHIC,
    CAMERA_PERSPECTIVE,
    KEY_A,
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
MOVE_KEYS = "A/D: x    W/S: z    Q/E: y"

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
            "Which way is the top of the picture.",
            "Tilt it and the picture rolls, like tilting your head.",
        ],
        "A/D: tilt",
    ),
    (
        "draw_model(model, position, scale, tint)",
        [
            "position places the centre of the cube.",
            "At y = 0 half the cube is under the floor. y = 0.5 sits on it.",
        ],
        MOVE_KEYS + "    Z/X: scale",
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


def reset():
    global point, cam_pos, cam_target, cam_roll, cam_fovy, cam_projection
    global cube_pos, cube_scale
    point = [3.0, 2.0, 2.0]
    cam_pos = [0.0, 10.0, 5.0]
    cam_target = [0.0, 0.0, 0.0]
    cam_roll = 0.0
    cam_fovy = 45.0
    cam_projection = CAMERA_PERSPECTIVE
    cube_pos = [0.0, 0.0, 0.0]
    cube_scale = 1.0


def move(v, dt):
    speed = 4 * dt
    v[0] += (is_key_down(KEY_D) - is_key_down(KEY_A)) * speed
    v[1] += (is_key_down(KEY_E) - is_key_down(KEY_Q)) * speed
    v[2] += (is_key_down(KEY_S) - is_key_down(KEY_W)) * speed


def cam_up():
    return [sin(cam_roll), cos(cam_roll), 0.0]


def draw_axes():
    draw_line_3d(V([0, 0, 0]), V([6, 0, 0]), RED)
    draw_line_3d(V([0, 0, 0]), V([0, 6, 0]), GREEN)
    draw_line_3d(V([0, 0, 0]), V([0, 0, 6]), BLUE)
    draw_sphere(V([6, 0, 0]), 0.1, RED)
    draw_sphere(V([0, 6, 0]), 0.1, GREEN)
    draw_sphere(V([0, 0, 6]), 0.1, BLUE)


def draw_scene():
    draw_grid(10, 1)
    draw_axes()
    draw_model(model, V(cube_pos), cube_scale, ORANGE)
    draw_model_wires(model, V(cube_pos), cube_scale, DARKBROWN)
    draw_line_3d(Vector3(-4, 0, -2), Vector3(5, 2, 3), MAROON)


def draw_point_path():
    x, y, z = point
    draw_line_3d(V([0, 0, 0]), V([x, 0, 0]), RED)
    draw_line_3d(V([x, 0, 0]), V([x, 0, z]), BLUE)
    draw_line_3d(V([x, 0, z]), V([x, y, z]), GREEN)
    draw_sphere(V(point), 0.15, PURPLE)


def draw_camera_gizmo():
    forward = norm(sub(cam_target, cam_pos))
    right = cross(forward, cam_up())
    right = norm(right) if length(right) > 0.0001 else [1, 0, 0]
    up = cross(right, forward)

    depth = max(length(sub(cam_target, cam_pos)), 1)
    aspect = INSET_W / INSET_H
    if cam_projection == CAMERA_PERSPECTIVE:
        half_h = depth * tan(radians(cam_fovy) / 2)
    else:
        half_h = cam_fovy / 2
    half_w = half_h * aspect

    far_center = add(cam_pos, scale(forward, depth))
    far, near = [], []
    for sx, sy in ((-1, 1), (1, 1), (1, -1), (-1, -1)):
        offset = add(scale(right, sx * half_w), scale(up, sy * half_h))
        far.append(add(far_center, offset))
        if cam_projection == CAMERA_PERSPECTIVE:
            near.append(cam_pos)
        else:
            near.append(add(cam_pos, offset))

    for i in range(4):
        draw_line_3d(V(near[i]), V(far[i]), SKYBLUE)
        draw_line_3d(V(far[i]), V(far[(i + 1) % 4]), SKYBLUE)
        draw_line_3d(V(near[i]), V(near[(i + 1) % 4]), SKYBLUE)

    draw_line_3d(V(cam_pos), V(cam_target), DARKGRAY)
    draw_line_3d(V(cam_pos), V(add(cam_pos, scale(cam_up(), 2))), LIME)
    draw_sphere(V(cam_pos), 0.25, BLACK)
    draw_sphere(V(cam_target), 0.15, PINK)


def label(text, world_pos, color):
    p = get_world_to_screen(V(world_pos), observer)
    draw_text(text, int(p.x) + 10, int(p.y) - 8, 18, color)


init_window(WINDOW_W, WINDOW_H, "Learn 3D")

mesh = gen_mesh_cube(1, 1, 1)
model = load_model_from_mesh(mesh)
inset = load_render_texture(INSET_W, INSET_H)

lesson = 0
reset()

orbit_yaw, orbit_pitch, orbit_dist = 0.7, 0.5, 24.0
observer = Camera3D()
observer.target = Vector3(0, 1, 0)
observer.up = Vector3(0, 1, 0)
observer.fovy = 45.0
observer.projection = CAMERA_PERSPECTIVE

camera = Camera3D()

while not window_should_close():
    dt = get_frame_time()

    # lesson switching
    if is_key_pressed(KEY_RIGHT):
        lesson = min(lesson + 1, len(LESSONS) - 1)
    if is_key_pressed(KEY_LEFT):
        lesson = max(lesson - 1, 0)
    if is_key_pressed(KEY_R):
        reset()

    # lesson controls
    if lesson == 0:
        move(point, dt)
    elif lesson == 1:
        move(cam_pos, dt)
    elif lesson == 2:
        move(cam_target, dt)
    elif lesson in (3, 4):
        cam_fovy += (is_key_down(KEY_W) - is_key_down(KEY_S)) * 30 * dt
        cam_fovy = max(1, min(cam_fovy, 120))
        if lesson == 4 and is_key_pressed(KEY_SPACE):
            if cam_projection == CAMERA_PERSPECTIVE:
                cam_projection, cam_fovy = CAMERA_ORTHOGRAPHIC, 10.0
            else:
                cam_projection, cam_fovy = CAMERA_PERSPECTIVE, 45.0
    elif lesson == 5:
        cam_roll += (is_key_down(KEY_D) - is_key_down(KEY_A)) * 1.5 * dt
    elif lesson == 6:
        move(cube_pos, dt)
        cube_scale += (is_key_down(KEY_X) - is_key_down(KEY_Z)) * 1.5 * dt
        cube_scale = max(0.1, min(cube_scale, 5))

    # the camera being taught
    camera.position = V(cam_pos)
    camera.target = V(cam_target)
    camera.up = V(cam_up())
    camera.fovy = cam_fovy
    camera.projection = cam_projection

    # the outside view: drag to orbit, wheel to zoom
    if is_mouse_button_down(MOUSE_BUTTON_LEFT):
        delta = get_mouse_delta()
        orbit_yaw -= delta.x * 0.005
        orbit_pitch = max(-1.5, min(orbit_pitch + delta.y * 0.005, 1.5))
    orbit_dist = max(5, min(orbit_dist - get_mouse_wheel_move() * 1.5, 60))
    observer.position = Vector3(
        orbit_dist * cos(orbit_pitch) * sin(orbit_yaw),
        orbit_dist * sin(orbit_pitch) + 1,
        orbit_dist * cos(orbit_pitch) * cos(orbit_yaw),
    )

    show_camera = lesson > 0

    # what the taught camera sees
    if show_camera:
        begin_texture_mode(inset)
        clear_background(WHITE)
        begin_mode_3d(camera)
        draw_scene()
        end_mode_3d()
        end_texture_mode()

    begin_drawing()
    clear_background(RAYWHITE)

    begin_mode_3d(observer)
    draw_scene()
    if show_camera:
        draw_camera_gizmo()
    else:
        draw_point_path()
    end_mode_3d()

    label("X", [6, 0, 0], RED)
    label("Y", [0, 6, 0], DARKGREEN)
    label("Z", [0, 0, 6], BLUE)
    if show_camera:
        label("camera.position", cam_pos, BLACK)
        label("camera.target", cam_target, MAROON)
        label("up", add(cam_pos, scale(cam_up(), 2)), DARKGREEN)
    else:
        label(fmt(point), point, PURPLE)

    # lesson text
    title, lines, keys = LESSONS[lesson]
    draw_text(f"{lesson + 1}/{len(LESSONS)}  {title}", 20, 20, 30, BLACK)
    for i, line in enumerate(lines):
        draw_text(line, 20, 64 + i * 26, 20, DARKGRAY)
    draw_text(keys, 20, 76 + len(lines) * 26, 20, DARKBLUE)

    # live code: the line this lesson changes is highlighted
    projection_name = (
        "CAMERA_PERSPECTIVE"
        if cam_projection == CAMERA_PERSPECTIVE
        else "CAMERA_ORTHOGRAPHIC"
    )
    code = [
        (f"point = {fmt(point)}", 0),
        (f"camera.position = {fmt(cam_pos)}", 1),
        (f"camera.target = {fmt(cam_target)}", 2),
        (f"camera.fovy = {cam_fovy:.1f}", 3),
        (f"camera.projection = {projection_name}", 4),
        (f"camera.up = {fmt(cam_up())}", 5),
        (f"draw_model(model, {fmt(cube_pos)}, {cube_scale:.1f}, ORANGE)", 6),
    ]
    code_y = WINDOW_H - 60 - len(code) * 24
    for i, (text, owner) in enumerate(code):
        active = owner == lesson or (owner == 3 and lesson == 4)
        draw_text(text, 20, code_y + i * 24, 20, RED if active else GRAY)

    draw_text(
        "LEFT/RIGHT: lesson    drag mouse: look around    wheel: zoom    R: reset",
        20,
        WINDOW_H - 30,
        18,
        DARKGRAY,
    )

    if show_camera:
        inset_x, inset_y = WINDOW_W - INSET_W - 20, WINDOW_H - INSET_H - 20
        draw_text("What this camera sees", inset_x, inset_y - 24, 18, BLACK)
        draw_texture_rec(
            inset.texture,
            Rectangle(0, 0, INSET_W, -INSET_H),
            Vector2(inset_x, inset_y),
            WHITE,
        )
        draw_rectangle_lines(inset_x - 1, inset_y - 1, INSET_W + 2, INSET_H + 2, BLACK)

    end_drawing()

unload_render_texture(inset)
close_window()
