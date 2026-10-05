from pyray import *

from raylib import CAMERA_PERSPECTIVE, KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP

init_window(1220, 680, "3D collisions")

camera = Camera3D()
camera.position = Vector3(0.0, 10, 10.0)
camera.target = Vector3(0.0, 0.0, 0.0)
camera.up = Vector3(0.0, 1.0, 0.0)
camera.fovy = 45.0
camera.projection = CAMERA_PERSPECTIVE

player_width = 1
player_length = 1
player_model = load_model_from_mesh(gen_mesh_cube(player_width, 1, player_length))
player_position = Vector3(0, 0, 3)
player_direction = Vector3(0, 0, 0)
player_speed = 1


def get_bounding_box(model: Model, position: Vector3) -> BoundingBox:
    bounding_box = get_mesh_bounding_box(model.meshes[0])
    min_boundary = vector3_add(position, bounding_box.min)
    max_boundary = vector3_add(position, bounding_box.max)
    return BoundingBox(min_boundary, max_boundary)


obstacle_width = 2
obstacle_length = 2
obstacle_model = load_model_from_mesh(gen_mesh_cube(obstacle_width, 2, obstacle_length))
obstacle_position = Vector3(0, 0, 0)

collision_axis = ""

while not window_should_close():
    # input
    player_direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
    player_direction.z = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))

    player_direction = vector3_normalize(player_direction)

    # movement & collision
    dt = get_frame_time()
    player_position.x += player_direction.x * player_speed * dt
    player_position.z += player_direction.z * player_speed * dt

    # collision
    player_bounding_box = get_bounding_box(player_model, player_position)
    obstacle_bounding_box = get_bounding_box(obstacle_model, obstacle_position)

    if not check_collision_boxes(player_bounding_box, obstacle_bounding_box):
        collision_axis = ""
    else:
        if collision_axis == "":
            # the axis with the smaller overlap is the one the player came in on
            overlap_x = (obstacle_width / 2 + player_width / 2) - abs(
                player_position.x - obstacle_position.x
            )
            overlap_z = (obstacle_length / 2 + player_length / 2) - abs(
                player_position.z - obstacle_position.z
            )
            collision_axis = "x" if overlap_x < overlap_z else "z"

        match collision_axis:
            case "x":
                if player_position.x < obstacle_position.x:
                    player_position.x = (
                        obstacle_position.x - obstacle_width / 2 - player_width / 2
                    )
                else:
                    player_position.x = (
                        obstacle_position.x + obstacle_width / 2 + player_width / 2
                    )
            case "z":
                if player_position.z < obstacle_position.z:
                    player_position.z = (
                        obstacle_position.z - obstacle_length / 2 - player_length / 2
                    )
                else:
                    player_position.z = (
                        obstacle_position.z + obstacle_length / 2 + player_length / 2
                    )

    # drawing
    begin_drawing()
    clear_background(WHITE)
    begin_mode_3d(camera)
    draw_grid(10, 1)
    draw_model(player_model, player_position, 1.0, RED)
    draw_model(obstacle_model, obstacle_position, 1.0, GRAY)
    draw_bounding_box(player_bounding_box, GREEN)
    end_mode_3d()
    end_drawing()
close_window()
