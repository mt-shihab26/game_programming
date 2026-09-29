from pyray import *
from os.path import join

window_weight = 1000
window_height = 700

init_window(window_weight, window_height, "Move")

spaceship_texture = load_texture(join("assets", "spaceship.png"))
spaceship_direction = Vector2(1, 0)
spaceship_position = Vector2(0, 0)
spaceship_speed = 200  # in 1 seconds how much pixel it should move

# set_target_fps(100)

while not window_should_close():
    delta_time = get_frame_time()

    # updates
    spaceship_position.x += spaceship_direction.x * spaceship_speed * delta_time
    spaceship_position.y += spaceship_direction.y * spaceship_speed * delta_time

    if spaceship_position.x < 0:
        spaceship_direction.x = 1

    if spaceship_position.x > window_weight:
        spaceship_direction.x = -1

    # drawing
    begin_drawing()
    clear_background(BLACK)
    draw_texture_v(spaceship_texture, spaceship_position, WHITE)
    draw_fps(0, 0)
    end_drawing()

unload_texture(spaceship_texture)

close_window()
