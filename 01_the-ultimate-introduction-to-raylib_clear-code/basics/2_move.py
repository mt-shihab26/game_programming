from pyray import *
from os.path import join

init_window(1000, 700, "Move")

spaceship_texture = load_texture(join("assets", "spaceship.png"))
spaceship_direction = Vector2(1, 1)
spaceship_position = Vector2(0, 0)
spaceship_speed = 500  # in 1 seconds how much pixel it should move

# set_target_fps(100)

while not window_should_close():
    delta_time = get_frame_time()
    screen_width = get_screen_width()
    screen_height = get_screen_height()

    # updates
    if spaceship_position.x < 0:
        spaceship_direction.x = 1

    if (spaceship_position.x + spaceship_texture.width) > screen_width:
        spaceship_direction.x = -1

    if spaceship_position.y < 0:
        spaceship_direction.y = 1

    if (spaceship_position.y + spaceship_texture.height) > screen_height:
        spaceship_direction.y = -1

    spaceship_position.x += spaceship_direction.x * spaceship_speed * delta_time
    spaceship_position.y += spaceship_direction.y * spaceship_speed * delta_time

    # drawing
    begin_drawing()
    draw_fps(screen_width - 105, 10)
    clear_background(BLACK)
    draw_texture_v(spaceship_texture, spaceship_position, WHITE)
    end_drawing()

unload_texture(spaceship_texture)

close_window()
