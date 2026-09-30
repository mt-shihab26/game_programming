from os.path import join
from pyray import *
from random import choice, randint

init_window(1000, 700, "Camera")


player_position = Vector2(0, 0)
player_radius = 50
player_direction = Vector2(0, 0)
player_speed = 400

circles = [
    (
        Vector2(randint(-2000, 2000), randint(-1000, 1000)),  # position
        randint(50, 200),  # radius
        choice([RED, GREEN, BLUE, YELLOW, ORANGE]),  # color
    )
    for i in range(100)
]

camera_object = Camera2D()
camera_zoom = 0
camera_object.zoom = 1
camera_direction = 0

while not window_should_close():
    # states
    delta_time = get_frame_time()
    screen_width = get_screen_width()
    screen_height = get_screen_height()

    # reset
    player_direction.x = 0
    player_direction.y = 0

    camera_direction = 0
    camera_zoom = 0

    # input
    if is_key_down(KeyboardKey.KEY_RIGHT):
        player_direction.x = 1
    if is_key_down(KeyboardKey.KEY_LEFT):
        player_direction.x = -1
    if is_key_down(KeyboardKey.KEY_DOWN):
        player_direction.y = 1
    if is_key_down(KeyboardKey.KEY_UP):
        player_direction.y = -1

    if is_key_down(KeyboardKey.KEY_S):
        camera_direction = 1
    if is_key_down(KeyboardKey.KEY_A):
        camera_direction = -1

    if is_key_down(KeyboardKey.KEY_Q):
        camera_zoom = 1
    if is_key_down(KeyboardKey.KEY_W):
        camera_zoom = -1

    # updates
    player_direction = vector2_normalize(player_direction)

    player_position.x += player_direction.x * player_speed * delta_time
    player_position.y += player_direction.y * player_speed * delta_time

    camera_object.target = player_position
    camera_object.offset = Vector2(screen_width / 2, screen_height / 2)
    camera_object.rotation += camera_direction * 50 * delta_time
    camera_object.zoom += camera_zoom * 2 * delta_time
    camera_object.zoom = max(0.2, min(2, camera_object.zoom))

    # drawing
    begin_drawing()
    begin_mode_2d(camera_object)
    clear_background(WHITE)
    draw_fps(screen_width - 105, 10)
    for circle in circles:
        draw_circle_v(*circle)
    draw_circle_v(player_position, player_radius, BLACK)
    end_mode_2d()
    end_drawing()


close_window()
