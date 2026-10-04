from pyray import *
from raylib import *

init_window(1920, 1080, "3D imports")
camera = Camera3D()
camera.position = Vector3(0.0, 3.0, 5.0) 
camera.target = Vector3(0.0, 0.0, 0.0) 
camera.up = Vector3(0.0, 1.0, 0.0) 
camera.fovy = 45.0 
camera.projection = CAMERA_PERSPECTIVE 

while not window_should_close():
    begin_drawing()    
    clear_background(WHITE)
    begin_mode_3d(camera)
    draw_grid(10,1.0)
    end_mode_3d()
    end_drawing()

close_window()