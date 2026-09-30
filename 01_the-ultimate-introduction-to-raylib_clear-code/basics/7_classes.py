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

    def update(self, delta_time: float) -> None:
        pass

    def draw(self) -> None:
        pass


class Player(Sprite):
    def __init__(self, position: Vector2) -> None:
        super().__init__(position, 500)
        self.texture = load_texture(join("assets", "spaceship.png"))

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

sprites: list[Sprite] = [
    Player(Vector2(500, 200)),
    Block(Vector2(0, 0), 200),
]

while not window_should_close():
    # states
    delta_time = get_frame_time()

    # updates
    for sprite in sprites:
        sprite.update(delta_time)

    # drawing
    begin_drawing()
    clear_background(BLACK)
    for sprite in sprites:
        sprite.draw()
    end_drawing()


close_window()
