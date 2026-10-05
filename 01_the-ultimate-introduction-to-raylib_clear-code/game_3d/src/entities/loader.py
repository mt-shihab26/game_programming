from pyray import Model, load_model
from os.path import abspath, dirname, join
from entity import Entity

ASSETS_DIR = join(dirname(dirname(abspath(__file__))), "assets")


class Loader(Entity):
    def __init__(self) -> None:
        self.models: dict[str, Model] = {
            "player": load_model(join(ASSETS_DIR, "models", "ship.glb")),
        }

    def close(self) -> None:
        pass

    def get_model(self, name: str) -> Model:
        return self.models[name]
