from core.controls import pressed_or_held

from pyray import KeyboardKey
from core.lesson import Lesson


class TextureLesson(Lesson):
    title = "set_material_texture(material, MATERIAL_MAP_ALBEDO, texture)"
    lines = [
        "So far every shape was a wire frame. draw_model fills it in.",
        "A texture is a picture wrapped around the model to colour it.",
        "ALBEDO is the model's base colour, before any light or effect.",
        "This picture is a gradient that fades from red to yellow.",
        "direction turns the fade, in degrees: at 0 it runs around the",
        "side of the cylinder, at 90 it runs from top to bottom.",
    ]
    keys = "A/D: direction"
    code = ("gen_image_gradient_linear", "set_material_texture")
    objects = ("textured_cylinder",)

    def update(self, delta_time: float) -> None:
        cylinder = self.scene.textured_cylinder
        cylinder.use(None)
        step = pressed_or_held(KeyboardKey.KEY_D) - pressed_or_held(KeyboardKey.KEY_A)
        cylinder.turn(step * 15)
