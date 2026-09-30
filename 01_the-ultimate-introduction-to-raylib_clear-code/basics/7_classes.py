from pyray import *
from os.path import join


class Sprite:
    def __init__(
        self, position: Vector2, speed: float, direction: Vector2 = Vector2(0, 0)
    ) -> None:
        self.position = position
        self.speed = speed
        self.direction = direction

    def move(self, delta_time):
        self.direction = vector2_normalize(self.direction)
        self.position.x += self.direction.x * self.speed * delta_time
        self.position.y += self.direction.y * self.speed * delta_time


class Player(Sprite):
    def __init__(self, position: Vector2) -> None:
        super().__init__(position, 500)
        self.texture = load_texture(join("assets", "spaceship.png"))
        self.direction = Vector2(0, 0)

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

        self.move(delta_time)

    def draw(self) -> None:
        draw_texture_v(self.texture, self.position, WHITE)


class Block(Sprite):
    def __init__(self, position: Vector2, speed: float) -> None:
        super().__init__(position, speed, Vector2(1, 0))
        self.size = Vector2(200, 100)

    def update(self, delta_time: float) -> None:
        self.move(delta_time)

    def draw(self) -> None:
        draw_rectangle_v(self.position, self.size, GREEN)


init_window(1000, 600, "OOP")

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
