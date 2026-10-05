from pyray import load_model, unload_model
from os.path import abspath, dirname, join

from pyray import Model
from core.entity import Entity

ASSETS_DIR = join(dirname(dirname(dirname(abspath(__file__)))), "assets")


class Loader(Entity):
    def __init__(self) -> None:
        self.models: dict[str, Model] = {
            "player": load_model(join(ASSETS_DIR, "models", "ship.glb")),
        }

    def close(self) -> None:
        for model in self.models.values():
            unload_model(model)

    def get_model(self, name: str) -> Model:
        return self.models[name]
