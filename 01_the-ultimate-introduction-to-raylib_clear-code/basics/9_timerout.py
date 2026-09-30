from pyray import *
from os.path import join
from random import choice
from typing import Callable


class Timer:
    def __init__(
        self,
        duration: float,
        repeat: bool = False,
        func: Callable[[], None] | None = None,
    ):
        self.duration = duration
        self.repeat = repeat
        self.func = func
        self.start_time = get_time()
        self.active = True

    def update(self):
        if not self.active:
            return
        if get_time() - self.start_time >= self.duration:
            if not self.repeat:
                self.active = False
            self.start_time = get_time()
            if self.func:
                self.func()


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
        self.color_timer = Timer(1.5, repeat=True, func=self.color_change)
        self.position_timer = Timer(4, repeat=True, func=self.position_change)

    def color_change(self):
        self.color = choice([RED, YELLOW, ORANGE, GRAY, BLACK, BLUE])

    def position_change(self):
        pass

    def update(self, delta_time: float) -> None:
        self.color_timer.update()
        self.position_timer.update()
        self.move(delta_time)

    def draw(self) -> None:
        draw_rectangle_v(self.position, self.size, self.color)


init_window(1000, 600, "Timerout")

set_target_fps(45)

sprites = [
    Block(Vector2(500, 200), 200),
]

while not window_should_close():
    # states
    delta_time = get_frame_time()

    # updates
    for sprite in sprites:
        sprite.update(delta_time)

    # drawing
    begin_drawing()
    clear_background(WHITE)
    for sprite in sprites:
        sprite.draw()
    end_drawing()


close_window()
