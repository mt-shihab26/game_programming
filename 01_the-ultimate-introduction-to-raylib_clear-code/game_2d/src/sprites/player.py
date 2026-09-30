from pyray import (
    WHITE,
    KeyboardKey,
    Vector2,
    draw_texture,
    draw_texture_v,
    get_screen_height,
    get_screen_width,
    is_key_down,
    load_texture,
    unload_texture,
    vector2_normalize,
)
from os.path import join

from core.config import PLAYER_SPEED
from core.sprite import Sprite


class Player(Sprite):
    def __init__(self) -> None:
        self.texture = load_texture(join("assets", "images", "spaceship.png"))
        self.direction = 0
        self.position = Vector2(
            (get_screen_width() / 2) - (self.texture.width / 2),
            (get_screen_height() * 5 / 6) - self.texture.height / 2,
        )
        self.speed = PLAYER_SPEED

    def deinit(self) -> None:
        unload_texture(self.texture)

    def update(self, delta_time: float) -> None:
        self.direction = 0
        if is_key_down(KeyboardKey.KEY_LEFT) or is_key_down(KeyboardKey.KEY_H):
            self.direction = -1
        if is_key_down(KeyboardKey.KEY_RIGHT) or is_key_down(KeyboardKey.KEY_L):
            self.direction = 1
        self.position.x += self.direction * self.speed * delta_time

    def draw(self) -> None:
        draw_texture_v(self.texture, self.position, WHITE)
