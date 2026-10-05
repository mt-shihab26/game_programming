from pyray import begin_drawing, begin_mode_3d, clear_background, close_window
from core.window import wait_for_window_size
from pyray import draw_grid, end_drawing, end_mode_3d, get_frame_time, init_window
from pyray import window_should_close

from core.entity import Entity
from entities.camera import Camera
from entities.loader import Loader
from entities.player import Player

from pyray import WHITE


class Game:
    def __init__(self) -> None:
        init_window(1220, 680, "Game 3D")

        wait_for_window_size()

        self.loader = Loader()
        self.camera = Camera()
        self.player = Player(self.loader.get_model("player"))

        self.entities: list[Entity] = [
            self.loader,
            self.camera,
            self.player,
        ]

    def close(self) -> None:
        for entity in self.entities:
            entity.close()
        close_window()

    def update(self, dt: float) -> None:
        for entity in self.entities:
            entity.update(dt)

    def draw(self) -> None:
        begin_drawing()
        begin_mode_3d(self.camera.object)
        clear_background(WHITE)
        draw_grid(10, 2)
        for entity in self.entities:
            entity.draw()
        end_mode_3d()
        end_drawing()

    def run(self) -> None:
        while not window_should_close():
            self.update(get_frame_time())
            self.draw()
        self.close()


if __name__ == "__main__":
    game = Game()
    game.run()
