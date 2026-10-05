from pyray import is_key_pressed

from pyray import KeyboardKey
from core.lesson import Lesson


class ShaderLesson(Lesson):
    title = "load_shader(vertex_file, fragment_file)"
    lines = [
        "A shader is a small program that runs on the graphics card.",
        "The fragment shader (a .fs file) runs once for every pixel of",
        "the model and decides its final colour.",
        "This one reads the texture colour and turns it into grey.",
        "The vertex file is left empty (ffi.NULL), so raylib uses its own.",
        "A shader does nothing until it is put on the model's material.",
    ]
    keys = "SPACE: shader on/off"
    code = ("load_shader", "material.shader", "grayscale.fs")
    objects = ("textured_cylinder",)

    def update(self, delta_time: float) -> None:
        cylinder = self.scene.textured_cylinder
        if is_key_pressed(KeyboardKey.KEY_SPACE):
            cylinder.gray = not cylinder.gray
        cylinder.use("grayscale" if cylinder.gray else None)
