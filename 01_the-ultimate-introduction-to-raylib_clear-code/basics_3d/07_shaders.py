from pyray import *
from os.path import join

from raylib import (
    CAMERA_PERSPECTIVE,
    KEY_A,
    MATERIAL_MAP_ALBEDO,
    SHADER_UNIFORM_VEC2,
    ffi,
)

init_window(1220, 680, "Shader")

camera = Camera3D()
camera.position = Vector3(0.0, 5.0, 5.0)
camera.target = Vector3(0.0, 0.0, 0.0)
camera.up = Vector3(0.0, 1.0, 0.0)
camera.fovy = 45.0
camera.projection = CAMERA_PERSPECTIVE

# create model
model = load_model_from_mesh(gen_mesh_cylinder(1, 2, 5))
texture = load_texture_from_image(gen_image_gradient_linear(100, 100, 1, RED, YELLOW))
set_material_texture(model.materials[0], MATERIAL_MAP_ALBEDO, texture)

# shaders

shader = load_shader(ffi.NULL, join("shaders", "flash.fs"))  # pyright: ignore[reportArgumentType]
model.materials[0].shader = shader

flash_location = get_shader_location(shader, "flash")
flash_amount = ffi.new("struct Vector2*", [1, 0])

while not window_should_close():
    if is_key_pressed(KEY_A):
        set_shader_value(shader, flash_location, flash_amount, SHADER_UNIFORM_VEC2)

    begin_drawing()
    begin_mode_3d(camera)
    clear_background(BLACK)
    draw_model(model, Vector3(0.0, 0.0, 0.0), 1.0, WHITE)
    end_mode_3d()
    end_drawing()
close_window()
