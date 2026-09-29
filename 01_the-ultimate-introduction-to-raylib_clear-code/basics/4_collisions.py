from os.path import join
from pyray import *

init_window(1000, 700, "Collisions")

# load
player_position = Vector2(0, 0)
obstacle_position = Vector2(500, 400)

player_radius = 50
obstacle_radius = 30

r1 = Rectangle(0, 0, 100, 200)
r2 = Rectangle(600, 400, 100, 200)

# loop
while not window_should_close():
    # states
    delta_time = get_frame_time()
    screen_width = get_screen_width()
    screen_height = get_screen_height()

    collision_rec = get_collision_rec(r1, r2)

    print(collision_rec.x, collision_rec.y, collision_rec.width, collision_rec.height)

    # input
    mouse_position = get_mouse_position()

    # updates
    player_position = mouse_position
    r1.x = mouse_position.x
    r1.y = mouse_position.y

    # drawing
    begin_drawing()
    clear_background(BLACK)
    draw_fps(screen_width - 105, 10)

    # draw_circle_v(player_position, player_radius, WHITE)
    draw_circle_v(obstacle_position, obstacle_radius, RED)
    draw_rectangle_rec(r1, BLUE)
    draw_rectangle_rec(r2, GREEN)

    end_drawing()

# unload

close_window()
