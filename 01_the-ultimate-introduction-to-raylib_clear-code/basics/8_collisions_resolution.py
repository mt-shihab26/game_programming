from pyray import *
from os.path import join

init_window(1300, 800, "Collisions Resolution")


def collision(
    axis: str, blocks: list[Rectangle], player: Rectangle, direction: Vector2
):
    for block in blocks:
        if check_collision_recs(block, player):
            if axis == "x":
                if 0 < direction.x:  # moving right
                    player.x = block.x - player.width
                if direction.x < 0:  # moving left
                    player.x = block.x + block.width
            else:
                if 0 < direction.y:  # moving bottom
                    player.y = block.y - player.height
                if direction.y < 0:  # moving top
                    player.y = block.y + block.height


player_rectangle = Rectangle(400, 300, 60, 60)
player_speed = 500
player_direction = Vector2(0, 0)


def get_blocks(screen_width: float, screen_height: float) -> list[Rectangle]:
    level_map = [
        "1111111111111111111",
        "1010000000000000001",
        "1010000000001111111",
        "1000000000000000111",
        "1000000200000000011",
        "1000000000000100001",
        "1000000000000100001",
        "1001100000000100001",
        "1001100000000100001",
        "1001100000000100001",
        "1111111111111111111",
    ]

    blocks: list[Rectangle] = []
    rows_len = len(level_map)
    columns_len = len(level_map[0])
    for i, row in enumerate(level_map):
        for j, column in enumerate(row):
            if column == "1":
                x_size = screen_width / columns_len
                y_size = screen_height / rows_len
                x_position = j * x_size
                y_position = i * y_size
                block = Rectangle(x_position, y_position, x_size, y_size)
                blocks.append(block)
    return blocks


while not window_should_close():
    # states
    screen_width = get_screen_width()
    screen_height = get_screen_height()
    delta_time = get_frame_time()
    blocks = get_blocks(screen_width, screen_height)

    # resets
    player_direction = Vector2(0, 0)

    # inputs
    if is_key_down(KeyboardKey.KEY_DOWN) or is_key_down(KeyboardKey.KEY_J):
        player_direction.y = 1
    if is_key_down(KeyboardKey.KEY_UP) or is_key_down(KeyboardKey.KEY_K):
        player_direction.y = -1
    if is_key_down(KeyboardKey.KEY_RIGHT) or is_key_down(KeyboardKey.KEY_L):
        player_direction.x = 1
    if is_key_down(KeyboardKey.KEY_LEFT) or is_key_down(KeyboardKey.KEY_H):
        player_direction.x = -1

    # updates
    player_direction = vector2_normalize(player_direction)

    player_rectangle.x += player_direction.x * player_speed * delta_time
    collision("x", blocks, player_rectangle, player_direction)

    player_rectangle.y += player_direction.y * player_speed * delta_time
    collision("y", blocks, player_rectangle, player_direction)

    # rendering
    begin_drawing()
    clear_background(WHITE)

    for block in blocks:
        draw_rectangle_rec(block, GRAY)

    draw_rectangle_rec(player_rectangle, BLACK)

    end_drawing()

close_window()
