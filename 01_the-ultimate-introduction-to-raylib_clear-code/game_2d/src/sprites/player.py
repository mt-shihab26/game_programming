from pyray import (
    WHITE,
    KeyboardKey,
    Vector2,
    draw_texture_v,
    get_screen_height,
    get_screen_width,
    is_key_down,
    load_texture,
    unload_texture,
)

from core.config import PLAYER_SPEED
from core.paths import spaceship_image_path
from core.entity import Entity
from core.sprite import Sprite
from entities.weapon import Weapon


class Player(Sprite):
    def __init__(self) -> None:
        super().__init__(
            spaceship_image_path(),
            Vector2(0, 0),
            PLAYER_SPEED,
            Vector2(0, 0),
        )
        self.position = Vector2(
            (get_screen_width() / 2) - (self.texture.width / 2),
            (get_screen_height() * 5 / 6) - self.texture.height / 2,
        )
        self.weapon = Weapon()

    def close(self) -> None:
        self.weapon.close()
        super().close()

    def update(self, delta_time: float) -> None:
        self.direction.x = 0

        if is_key_down(KeyboardKey.KEY_LEFT) or is_key_down(KeyboardKey.KEY_H):
            self.direction.x = -1
        if is_key_down(KeyboardKey.KEY_RIGHT) or is_key_down(KeyboardKey.KEY_L):
            self.direction.x = 1

        super().update(delta_time)

        if get_screen_width() < self.position.x + self.texture.width:
            self.position.x = get_screen_width() - self.texture.width
        if self.position.x < 0:
            self.position.x = 0

        self.weapon.update(
            delta_time, self.position.x + (self.texture.width / 2), self.position.y
        )

    def draw(self) -> None:
        super().draw()
        self.weapon.draw()
