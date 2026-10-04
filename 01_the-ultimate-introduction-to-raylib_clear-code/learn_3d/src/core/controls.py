from pyray import is_key_down, is_key_pressed, is_key_pressed_repeat

from pyray import KeyboardKey
from core.vector import Vec

from core.config import MOVE_SPEED

MOVE_KEYS = "A/D: x    Q/E: y    W/S: z"


def axis(positive: int, negative: int) -> int:
    return is_key_down(positive) - is_key_down(negative)


def pressed_or_held(key: int) -> bool:
    # true on the first press, then again and again while the key stays down
    return is_key_pressed(key) or is_key_pressed_repeat(key)


def move(v: Vec, delta_time: float, speed: float = MOVE_SPEED) -> None:
    v[0] += axis(KeyboardKey.KEY_D, KeyboardKey.KEY_A) * speed * delta_time
    v[1] += axis(KeyboardKey.KEY_E, KeyboardKey.KEY_Q) * speed * delta_time
    v[2] += axis(KeyboardKey.KEY_S, KeyboardKey.KEY_W) * speed * delta_time
