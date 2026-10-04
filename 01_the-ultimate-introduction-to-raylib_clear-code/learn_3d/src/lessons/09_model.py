from core.controls import MOVE_KEYS, axis, move

from pyray import KeyboardKey
from core.lesson import Lesson

from core.config import SCALE_SPEED


class ModelLesson(Lesson):
    title = "draw_model(model, position, scale, tint)"
    lines = [
        "position places the centre of the cube.",
        "At y = 0 half the cube is under the floor. y = 0.5 sits on it.",
    ]
    keys = MOVE_KEYS + "    Z/X: scale"
    code = ("draw_model",)
    objects = ("cube",)

    def update(self, delta_time: float) -> None:
        cube = self.scene.cube
        move(cube.pos, delta_time)
        amount = axis(KeyboardKey.KEY_X, KeyboardKey.KEY_Z)
        cube.resize(amount * SCALE_SPEED * delta_time)
