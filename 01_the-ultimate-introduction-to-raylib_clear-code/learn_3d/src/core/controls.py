from pyray import is_key_down, is_key_pressed, is_key_pressed_repeat

from pyray import KeyboardKey
from core.vector import Vec

from core.config import MOVE_SPEED

MOVE_KEYS = "A/D or H/L: x    Q/E: y    W/S or K/J: z"


def axis(positive: int, negative: int) -> int:
    return is_key_down(positive) - is_key_down(negative)


def pressed_or_held(key: int) -> bool:
    # true on the first press, then again and again while the key stays down
    return is_key_pressed(key) or is_key_pressed_repeat(key)


def move(v: Vec, delta_time: float, speed: float = MOVE_SPEED) -> None:
    # vim keys work too: H/L is left/right, K/J is away/toward you
    x = axis(KeyboardKey.KEY_D, KeyboardKey.KEY_A) or axis(
        KeyboardKey.KEY_L, KeyboardKey.KEY_H
    )
    y = axis(KeyboardKey.KEY_E, KeyboardKey.KEY_Q)
    z = axis(KeyboardKey.KEY_S, KeyboardKey.KEY_W) or axis(
        KeyboardKey.KEY_J, KeyboardKey.KEY_K
    )
    v[0] += x * speed * delta_time
    v[1] += y * speed * delta_time
    v[2] += z * speed * delta_time
