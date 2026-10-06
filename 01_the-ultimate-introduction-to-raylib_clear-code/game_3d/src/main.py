from pyray import begin_drawing, begin_mode_3d, clear_background, close_window
from core.timer import Timer
from core.window import wait_for_window_size
from pyray import draw_grid, end_drawing, end_mode_3d, get_frame_time, init_window
from pyray import window_should_close

from core.entity import Entity
from entities.camera import Camera
from entities.loader import Loader
from entities.obstacle import Obstacle
from entities.player import Player
from core.timer import Timer

from pyray import WHITE


class Game:
    def __init__(self) -> None:
        init_window(1220, 680, "Game 3D")

        wait_for_window_size()

        self.obstacle_timer = Timer(duration=0.5, func=self.add_obstacle)

        self.obstacles: list[Obstacle] = []

        self.loader = Loader()
        self.camera = Camera()
        self.player = Player(self.loader.get_model("player"))

        self.add_obstacle()

    def close(self) -> None:
        for entity in self.entities():
            entity.close()
        close_window()

    def update(self, dt: float) -> None:
        self.obstacle_timer.update()
        for entity in self.entities():
            entity.update(dt)

    def draw(self) -> None:
        begin_drawing()
        begin_mode_3d(self.camera.object)
        clear_background(WHITE)
        draw_grid(10, 2)
        for entity in self.entities():
            entity.draw()
        end_mode_3d()
        end_drawing()

    def run(self) -> None:
        while not window_should_close():
            self.update(get_frame_time())
            self.draw()
        self.close()

    def entities(self) -> list[Entity]:
        return [
            self.loader,
            self.camera,
            self.player,
        ] + self.obstacles

    def add_obstacle(self):
        self.obstacles.append(Obstacle())


if __name__ == "__main__":
    game = Game()
    game.run()
