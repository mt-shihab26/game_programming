from os.path import join
from pyray import *

init_window(1000, 700, "Input")

# load
spaceship_texture = load_texture(join("assets", "spaceship.png"))
spaceship_direction = Vector2(0, 0)
spaceship_position = Vector2(0, 0)
spaceship_speed = 500

# loop
while not window_should_close():
    # states
    delta_time = get_frame_time()
    screen_width = get_screen_width()
    screen_height = get_screen_height()

    # reset
    spaceship_direction.x = 0
    spaceship_direction.y = 0

    # input
    if is_key_down(KeyboardKey.KEY_RIGHT):
        spaceship_direction.x = 1
    if is_key_down(KeyboardKey.KEY_LEFT):
        spaceship_direction.x = -1
    if is_key_down(KeyboardKey.KEY_DOWN):
        spaceship_direction.y = 1
    if is_key_down(KeyboardKey.KEY_UP):
        spaceship_direction.y = -1

    # updates
    spaceship_direction = vector2_normalize(spaceship_direction)

    spaceship_position.x += spaceship_direction.x * spaceship_speed * delta_time
    spaceship_position.y += spaceship_direction.y * spaceship_speed * delta_time

    # drawing
    begin_drawing()
    draw_fps(screen_width - 105, 10)
    clear_background(BLACK)
    draw_texture_v(spaceship_texture, spaceship_position, WHITE)
    end_drawing()

# unload
unload_texture(spaceship_texture)

close_window()
