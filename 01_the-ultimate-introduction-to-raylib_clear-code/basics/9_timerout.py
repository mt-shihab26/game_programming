from pyray import *
from os.path import join
from random import choice


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


class Block(Sprite):
    def __init__(self, position: Vector2, speed: float) -> None:
        super().__init__(position, speed, Vector2(0, 0))
        self.size = Vector2(200, 100)
        self.color = GREEN

    def update(self, delta_time: float, change_color: bool) -> None:
        self.move(delta_time)
        if change_color:
            self.color = choice([RED, YELLOW, ORANGE, GRAY, BLACK, BLUE])

    def draw(self) -> None:
        draw_rectangle_v(self.position, self.size, self.color)


init_window(1000, 600, "Timerout")

set_target_fps(45)

sprites = [
    Block(Vector2(500, 200), 200),
]

count = 1

while not window_should_close():
    # states
    delta_time = get_frame_time()
    time = get_time()

    prev_count = count
    diff_time = time / count
    if diff_time >= 1.5:
        print(time, diff_time, True)
        count += 1

    # updates
    for sprite in sprites:
        sprite.update(delta_time, count != prev_count)

    # drawing
    begin_drawing()
    clear_background(WHITE)
    for sprite in sprites:
        sprite.draw()
    end_drawing()


close_window()
