from pyray import load_model, load_music_stream, unload_model
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

    def close(self) -> None:
        for model in self.models.values():
            unload_model(model)

    def get_model(self, name: str) -> Model:
        return self.models[name]

    def get_music(self, name: str) -> Music:
        return self.musics[name]
