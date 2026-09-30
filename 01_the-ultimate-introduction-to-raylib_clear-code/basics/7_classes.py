from pyray import *
from os.path import join


class Player:
    def __init__(self, position: Vector2) -> None:
        self.position = position
        self.texture = load_texture(join("assets", "spaceship.png"))
        self.direction = Vector2(0, 0)
        self.speed = 500

    def update(self, delta_time: float) -> None:
        self.direction.x = 0
        self.direction.y = 0

        if is_key_down(KeyboardKey.KEY_RIGHT):
            self.direction.x = 1
        if is_key_down(KeyboardKey.KEY_LEFT):
            self.direction.x = -1
        if is_key_down(KeyboardKey.KEY_DOWN):
            self.direction.y = 1
        if is_key_down(KeyboardKey.KEY_UP):
            self.direction.y = -1

        self.direction = vector2_normalize(self.direction)
        self.position.x += self.direction.x * self.speed * delta_time
        self.position.y += self.direction.y * self.speed * delta_time

    def draw(self) -> None:
        draw_texture_v(self.texture, self.position, WHITE)


class Block:
    def __init__(self, position: Vector2, speed: float) -> None:
        self.speed = speed
        self.rectangle = Rectangle(position.x, position.y, 200, 100)
        self.direction = Vector2(1, 0)

    def update(self, delta_time: float) -> None:
        self.direction = vector2_normalize(self.direction)

        self.rectangle.x += self.direction.x * self.speed * delta_time
        self.rectangle.y += self.direction.y * self.speed * delta_time

    def draw(self) -> None:
        draw_rectangle_rec(self.rectangle, GREEN)


init_window(1000, 600, "Audio")

player = Player(Vector2(500, 200))
block = Block(Vector2(0, 0), 200)

while not window_should_close():
    # states
    delta_time = get_frame_time()

    # updates
    player.update(delta_time)
    block.update(delta_time)

    # drawing
    begin_drawing()
    clear_background(BLACK)
    player.draw()
    block.draw()
    end_drawing()


close_window()
