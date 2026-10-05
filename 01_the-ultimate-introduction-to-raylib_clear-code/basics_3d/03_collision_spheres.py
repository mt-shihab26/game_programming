from pyray import *

from raylib import CAMERA_PERSPECTIVE, KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP

init_window(1220, 680, "3D collisions")

camera = Camera3D()
camera.position = Vector3(0.0, 5.0, 5.0)
camera.target = Vector3(0.0, 0.0, 0.0)
camera.up = Vector3(0.0, 1.0, 0.0)
camera.fovy = 45.0
camera.projection = CAMERA_PERSPECTIVE

player = load_model_from_mesh(gen_mesh_sphere(0.5, 12, 12))
player_position = Vector3(0, 0, 0)
player_direction = Vector3(0, 0, 0)
player_speed = 5

obstacle = load_model_from_mesh(gen_mesh_sphere(2, 12, 12))
obstacle_position = Vector3(3, 0, 0)

while not window_should_close():
    # input
    player_direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
    player_direction.z = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))

    # movement & collision
    dt = get_frame_time()
    player_position.x += player_direction.x * player_speed * dt
    player_position.z += player_direction.z * player_speed * dt

    # collision
    print(check_collision_spheres(player_position, 0.5, obstacle_position, 2))

    # drawing
    begin_drawing()
    clear_background(WHITE)
    begin_mode_3d(camera)
    draw_grid(10, 1)
    draw_model(player, player_position, 1.0, RED)
    draw_model(obstacle, obstacle_position, 1.0, GRAY)
    end_mode_3d()
    end_drawing()
close_window()
