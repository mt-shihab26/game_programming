from pyray import (
    KeyboardKey,
    Texture,
    Vector2,
    get_screen_height,
    get_screen_width,
    is_key_down,
)

from core.config import PLAYER_SPEED
from core.paths import spaceship_image_path
from core.sprite import Sprite
from entities.weapon import Weapon


class Player(Sprite):
    def __init__(self, texture: Texture) -> None:
        super().__init__(
            texture=texture,
            position=Vector2(
                (get_screen_width() / 2) - (texture.width / 2),
                (get_screen_height() * 5 / 6) - (texture.height / 2),
            ),
            speed=PLAYER_SPEED,
            direction=Vector2(0, 0),
        )
        self.weapon = Weapon()
        self.shoot = False

    def close(self) -> None:
        self.weapon.close()
        super().close()

    def update(self, delta_time: float) -> None:
        self.handle_movement()
        self.handle_shooting()
        self.handle_not_out_of_screen()

        self.weapon.update(
            delta_time,
            self.position.x + (self.size.x / 2),
            self.position.y,
            self.shoot,
        )

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
        if is_key_down(KeyboardKey.KEY_SPACE):
            self.shoot = True
        else:
            self.shoot = False

    def handle_not_out_of_screen(self):
        if get_screen_width() < self.position.x + self.size.x:
            self.position.x = get_screen_width() - self.size.x
        if self.position.x < 0:
            self.position.x = 0
        if get_screen_height() < self.position.y + self.size.y:
            self.position.y = get_screen_height() - self.size.y
        if self.position.y < 0:
            self.position.y = 0

    def draw(self) -> None:
        super().draw()
        self.weapon.draw()
