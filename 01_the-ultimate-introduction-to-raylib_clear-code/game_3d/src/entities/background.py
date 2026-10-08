from pyray import (
    Texture,
    Vector3,
    gen_mesh_cube,
    load_model_from_mesh,
    play_music_stream,
    set_material_texture,
    update_music_stream,
)

from pyray import Music
from raylib import MATERIAL_MAP_ALBEDO, Vector2Add
from core.sprite import Sprite


class Background(Sprite):
    def __init__(self, texture: Texture, music: Music) -> None:
        model = load_model_from_mesh(gen_mesh_cube(32, 1, 32))
        set_material_texture(model.materials[0], MATERIAL_MAP_ALBEDO, texture)
        super().__init__(model)
        self.music = music
        play_music_stream(music)

    def update(self, dt) -> None:
        update_music_stream(self.music)
