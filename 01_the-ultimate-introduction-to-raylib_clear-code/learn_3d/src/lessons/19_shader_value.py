from core.controls import axis

from pyray import KeyboardKey
from core.lesson import Lesson

from core.config import FLASH_SPEED


class ShaderValueLesson(Lesson):
    title = "set_shader_value(shader, location, value, type)"
    lines = [
        "A uniform is a value you send from Python into the shader.",
        "get_shader_location finds it by the name used in the .fs file.",
        "The shader keeps the value until you send a new one.",
        "Here flash.x mixes the texture colour with white:",
        "0 is the texture, 1 is fully white. Handy for a hit flash.",
    ]
    keys = "W/S: flash"
    code = ("get_shader_location", "flash_amount", "set_shader_value", "flash.fs")
    objects = ("textured_cylinder",)

    def update(self, delta_time: float) -> None:
        cylinder = self.scene.textured_cylinder
        cylinder.use("flash")
        amount = axis(KeyboardKey.KEY_W, KeyboardKey.KEY_S)
        cylinder.change_flash(amount * FLASH_SPEED * delta_time)
