from pyray import *
from raylib import *

init_window(1920, 1080, "3D collisions")
camera = Camera3D()
camera.position = Vector3(0.0, 5.0, 5.0) 
camera.target = Vector3(0.0, 0.0, 0.0) 
camera.up = Vector3(0.0, 1.0, 0.0) 
camera.fovy = 45.0 
camera.projection = CAMERA_PERSPECTIVE 

player = load_model_from_mesh(gen_mesh_cube(1,1,1))
pos = Vector3()
direction = Vector3()
speed = 5

obstacle = load_model_from_mesh(gen_mesh_cube(2,1,4))
obstacle_pos = Vector3(3,0,0)

while not window_should_close():
    # input
    direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
    direction.z = int(is_key_down(KEY_DOWN))  - int(is_key_down(KEY_UP))

    # movement & collision
    dt = get_frame_time()
    pos.x += direction.x * speed * dt
    pos.z += direction.z * speed * dt
    
    # drawing
    begin_drawing()
    clear_background(WHITE)
    begin_mode_3d(camera)
    draw_grid(10,1)
    draw_model(player, pos,1.0,RED)
    draw_model(obstacle, obstacle_pos,1.0,GRAY)
    end_mode_3d()
    end_drawing()
close_window()