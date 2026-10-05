from pathlib import Path
from pyray import draw_model, gen_image_gradient_linear, gen_mesh_cylinder
from pyray import get_shader_location, load_model_from_mesh, load_shader
from pyray import load_texture_from_image, set_material_texture, set_shader_value
from pyray import unload_image, unload_model, unload_shader, unload_texture

from pyray import MaterialMapIndex, Shader, ShaderUniformDataType, Texture, ffi
from core.entity import Entity
from core.vector import V

from pyray import RED, WHITE, YELLOW

SHADERS_DIR = Path(__file__).resolve().parent.parent.joinpath("shaders")


class TexturedCylinder(Entity):
    """A solid cylinder with a gradient texture, for the shaders to work on."""

    def __init__(self) -> None:
        self.pos = [0.0, 0.0, 0.0]
        self.set_defaults()
        self.model = load_model_from_mesh(gen_mesh_cylinder(1, 2, 20))
        self.texture = self.build_texture()
        self.set_texture()

        material = self.model.materials[0]
        # a copy of raylib's own shader, to switch back to
        self.default_shader = Shader(material.shader.id, material.shader.locs)
        # no vertex shader file (NULL) means raylib uses its own
        self.shaders = {
            name: load_shader(ffi.NULL, str(SHADERS_DIR.joinpath(f"{name}.fs")))
            for name in ("grayscale", "flash")
        }
        self.flash_location = get_shader_location(self.shaders["flash"], "flash")

    def set_defaults(self) -> None:
        self.direction = 0
        self.gray = True
        self.flash = 0.0

    def build_texture(self) -> Texture:
        image = gen_image_gradient_linear(100, 100, self.direction, RED, YELLOW)
        texture = load_texture_from_image(image)
        unload_image(image)
        return texture

    def set_texture(self) -> None:
        set_material_texture(
            self.model.materials[0], MaterialMapIndex.MATERIAL_MAP_ALBEDO, self.texture
        )

    def retexture(self) -> None:
        # the gradient is baked into the picture, so a new direction needs a new one
        unload_texture(self.texture)
        self.texture = self.build_texture()
        self.set_texture()

    def send_flash(self) -> None:
        # the shader wants a vec2, so the amount goes in as its x
        value = ffi.new("struct Vector2 *", [self.flash, 0])
        set_shader_value(
            self.shaders["flash"],
            self.flash_location,
            value,
            ShaderUniformDataType.SHADER_UNIFORM_VEC2,
        )

    def reset(self) -> None:
        self.set_defaults()
        self.retexture()
        self.send_flash()

    def turn(self, degrees: int) -> None:
        if not degrees:
            return
        self.direction = (self.direction + degrees) % 360
        self.retexture()

    def change_flash(self, amount: float) -> None:
        if not amount:
            return
        self.flash = max(0.0, min(self.flash + amount, 1.0))
        self.send_flash()

    def use(self, name: str | None) -> None:
        # None is raylib's own shader, which just draws the texture
        shader = self.default_shader if name is None else self.shaders[name]
        self.model.materials[0].shader = shader

    def close(self) -> None:
        # unload_model also unloads the material's shader and texture,
        # so hand it raylib's own shader and unload ours by hand
        self.use(None)
        for shader in self.shaders.values():
            unload_shader(shader)
        unload_model(self.model)

    def draw(self) -> None:
        draw_model(self.model, V(self.pos), 1, WHITE)
