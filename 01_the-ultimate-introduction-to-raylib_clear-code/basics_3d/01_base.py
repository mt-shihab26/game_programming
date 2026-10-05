from pyray import *
from raylib import CAMERA_PERSPECTIVE, MATERIAL_MAP_ALBEDO

init_window(1220, 680, "3D base")

camera = Camera3D()
camera.position = Vector3(0.0, 10.0, 10.0)
camera.target = Vector3(0.0, 0.0, 0.0)
camera.up = Vector3(0.0, 10.0, 0.0)
camera.fovy = 45.0
camera.projection = CAMERA_PERSPECTIVE

mesh = gen_mesh_cube(1, 1, 1)
model = load_model_from_mesh(mesh)

cylinder_mesh = gen_mesh_cylinder(1, 2, 50)
cylinder_model = load_model_from_mesh(cylinder_mesh)

image = gen_image_gradient_linear(20, 20, 1, RED, YELLOW)
image_texture = load_texture_from_image(image)

set_material_texture(cylinder_model.materials[0], MATERIAL_MAP_ALBEDO, image_texture)

position = Vector3(0, 0, 0)
rotation = 0
while not window_should_close():
    dt = get_frame_time()

    # position.x += dt * 1
    # position.y += dt * 1
    # position.z += dt * 1

    rotation += dt * 4

    cylinder_model.transform = matrix_rotate_x(rotation)

    clear_background(WHITE)
    begin_drawing()

    begin_mode_3d(camera)

    draw_grid(10, 1)

    draw_model(cylinder_model, position, 1, WHITE)

    end_mode_3d()

    end_drawing()

close_window()
