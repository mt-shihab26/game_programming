from pyray import Model, load_model
from os.path import join

from entity import Entity


class Loader(Entity):
    def __init__(self) -> None:
        self.models: dict[str, Model] = {
            "player": load_model(join("assets", "models", "ship.glb")),
        }

    def close(self) -> None:
        pass

    def get_model(self, name: str) -> Model:
        return self.models[name]
