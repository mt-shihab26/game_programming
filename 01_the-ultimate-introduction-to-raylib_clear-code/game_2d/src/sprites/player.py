from pyray import get_screen_height, get_screen_width, is_key_down, is_key_pressed

from pyray import KeyboardKey, Texture, Vector2
from core.sprite import Sprite
from typing import Callable

from core.config import PLAYER_SPEED


class Player(Sprite):
    def __init__(self, texture: Texture, on_shoot: Callable[[Vector2], None]) -> None:
        super().__init__(
            texture=texture,
            position=Vector2(
                (get_screen_width() / 2) - (texture.width / 2),
                (get_screen_height() * 5 / 6) - (texture.height / 2),
            ),
            speed=PLAYER_SPEED,
            direction=Vector2(0, 0),
        )
        self.on_shoot = on_shoot

    def update(self, delta_time: float) -> None:
        self.handle_movement()
        self.handle_shooting()
        self.position = self.constraint()
        super().update(delta_time)

    def handle_movement(self):
        self.direction.x = 0
        self.direction.y = 0

        if is_key_down(KeyboardKey.KEY_LEFT) or is_key_down(KeyboardKey.KEY_H):
            self.direction.x = -1
        if is_key_down(KeyboardKey.KEY_RIGHT) or is_key_down(KeyboardKey.KEY_L):
            self.direction.x = 1

        if is_key_down(KeyboardKey.KEY_UP) or is_key_down(KeyboardKey.KEY_K):
            self.direction.y = -1
        if is_key_down(KeyboardKey.KEY_DOWN) or is_key_down(KeyboardKey.KEY_J):
            self.direction.y = 1

    def handle_shooting(self):
        if is_key_pressed(KeyboardKey.KEY_SPACE):
            self.on_shoot(Vector2(self.position.x + (self.size.x / 2), self.position.y))
