from os.path import join
from pyray import *

init_window(1000, 700, "Collisions")

# load
player_position = Vector2(0, 0)
obstacle_position = Vector2(500, 400)

player_radius = 50
obstacle_radius = 30

# loop
while not window_should_close():
    # states
    delta_time = get_frame_time()
    screen_width = get_screen_width()
    screen_height = get_screen_height()

    # reset

    # input
    mouse_position = get_mouse_position()

    # updates
    player_position = mouse_position

    # drawing
    begin_drawing()
    clear_background(BLACK)
    draw_fps(screen_width - 105, 10)

    draw_circle_v(player_position, player_radius, WHITE)
    draw_circle_v(obstacle_position, obstacle_radius, RED)

    end_drawing()

# unload

close_window()
