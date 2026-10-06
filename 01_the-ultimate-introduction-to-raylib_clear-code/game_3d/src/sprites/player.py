from pyray import is_key_down, is_key_pressed

from pyray import Model, Vector3, KeyboardKey
from core.sprite import Sprite
from collections.abc import Callable


class Player(Sprite):
    def __init__(self, model: Model, on_shoot: Callable[[Vector3], None]) -> None:
        super().__init__(
            model=model,
            position=Vector3(0, 0, 7.5),
            direction=Vector3(0, 0, 0),
            speed=15,
        )
        self.on_shoot = on_shoot

    def update(self, dt: float) -> None:
        self.movement()
        super().update(dt)

    def movement(self) -> None:
        left = is_key_down(KeyboardKey.KEY_LEFT) or is_key_down(KeyboardKey.KEY_H)
        right = is_key_down(KeyboardKey.KEY_RIGHT) or is_key_down(KeyboardKey.KEY_L)
        up = is_key_down(KeyboardKey.KEY_UP) or is_key_down(KeyboardKey.KEY_K)
        down = is_key_down(KeyboardKey.KEY_DOWN) or is_key_down(KeyboardKey.KEY_J)

        self.direction.x = int(right) - int(left)
        self.direction.z = int(down) - int(up)

        if is_key_pressed(KeyboardKey.KEY_SPACE):
            size = self.size()

            self.on_shoot(
                Vector3(
                    self.position.x,
                    self.position.y + (size["height"] / 2),
                    self.position.z - (size["depth"] / 2),
                )
            )
