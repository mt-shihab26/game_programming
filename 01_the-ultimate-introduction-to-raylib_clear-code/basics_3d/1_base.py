from pyray import *
from raylib import CAMERA_PERSPECTIVE

init_window(1220, 680, "3D base")

camera = Camera3D()
camera.position = Vector3(0, 5.0, 5.0)
camera.target = Vector3(0, 0, 0)
camera.up = Vector3(0, 1, 0)
camera.fovy = 45.0
camera.projection = CAMERA_PERSPECTIVE

while not window_should_close():
    dt = get_frame_time()

    clear_background(WHITE)
    begin_drawing()

    begin_mode_3d(camera)

    draw_grid(10, 1)

    end_mode_3d()

    end_drawing()

close_window()
