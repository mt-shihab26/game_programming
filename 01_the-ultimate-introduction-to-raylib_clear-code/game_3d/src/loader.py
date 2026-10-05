from pyray import Model

from entity import Entity


class Loader(Entity):
    def __init__(self) -> None:
        pass

    def close(self) -> None:
        pass

    def get_model(self, name: str) -> Model:
        return Model()
