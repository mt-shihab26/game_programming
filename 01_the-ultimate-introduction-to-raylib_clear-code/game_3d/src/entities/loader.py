from pyray import (
    Sound,
    Texture,
    load_model,
    load_music_stream,
    load_sound,
    load_texture,
    unload_model,
    unload_music_stream,
    unload_sound,
    unload_texture,
)
from os.path import abspath, dirname, join

from pyray import Model, Music
from core.entity import Entity

ASSETS_DIR = join(dirname(dirname(dirname(abspath(__file__)))), "assets")


class Loader(Entity):
    def __init__(self) -> None:
        self.models: dict[str, Model] = {
            "player": load_model(join(ASSETS_DIR, "models", "ship.glb")),
            "laser": load_model(join(ASSETS_DIR, "models", "laser.glb")),
        }
        self.musics: dict[str, Music] = {
            "background": load_music_stream(join(ASSETS_DIR, "audios", "music.wav")),
        }
        self.sounds: dict[str, Sound] = {
            "laser": load_sound(join(ASSETS_DIR, "audios", "laser.wav")),
        }
        self.textures: dict[str, Texture] = {
            "dark": load_texture(join(ASSETS_DIR, "textures", "dark.png")),
            "green": load_texture(join(ASSETS_DIR, "textures", "green.png")),
            "light": load_texture(join(ASSETS_DIR, "textures", "light.png")),
            "orange": load_texture(join(ASSETS_DIR, "textures", "orange.png")),
            "purple": load_texture(join(ASSETS_DIR, "textures", "purple.png")),
            "red": load_texture(join(ASSETS_DIR, "textures", "red.png")),
        }

    def close(self) -> None:
        for model in self.models.values():
            unload_model(model)
        for music in self.musics.values():
            unload_music_stream(music)
        for sound in self.sounds.values():
            unload_sound(sound)
        for texture in self.textures.values():
            unload_texture(texture)

    def get_model(self, name: str) -> Model:
        return self.models[name]

    def get_music(self, name: str) -> Music:
        return self.musics[name]

    def get_sound(self, name: str) -> Sound:
        return self.sounds[name]

    def get_texture(self, name: str) -> Texture:
        return self.textures[name]
