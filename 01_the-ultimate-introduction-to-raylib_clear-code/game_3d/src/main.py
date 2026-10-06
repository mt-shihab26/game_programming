from pyray import (
    Vector3,
    close_audio_device,
    draw_fps,
    begin_drawing,
    begin_mode_3d,
    clear_background,
)
from pyray import draw_grid, end_drawing, end_mode_3d, get_frame_time, init_window
from pyray import window_should_close, set_target_fps, close_window, init_audio_device
from core.window import wait_for_window_size

from core.entity import Entity
from core.timer import Timer
from entities.background import Background
from entities.camera import Camera
from entities.loader import Loader
from sprites.laser import Laser
from sprites.player import Player
from sprites.obstacle import Obstacle

from pyray import WHITE


class Game:
    def __init__(self) -> None:
        init_window(1220, 680, "Game 3D")
        init_audio_device()

        set_target_fps(60)

        wait_for_window_size()

        self.obstacle_timer = Timer(duration=1, func=self.add_obstacle)

        self.obstacles: list[Obstacle] = []
        self.lasers: list[Laser] = []

        self.loader = Loader()
        self.camera = Camera()
        self.background = Background(self.loader.get_music("background"))
        self.player = Player(self.loader.get_model("player"), self.add_laser)

        self.add_obstacle()

    def close(self) -> None:
        for entity in self.entities():
            entity.close()
        close_audio_device()
        close_window()

    def update(self, dt: float) -> None:
        self.handle_remove_obsticale_out_of_screen()
        self.obstacle_timer.update()
        for entity in self.entities():
            entity.update(dt)

    def handle_remove_obsticale_out_of_screen(self):
        obstacles: list[Obstacle] = []
        for obstacle in self.obstacles:
            if obstacle.position.z > 30:
                obstacle.close()
            else:
                obstacles.append(obstacle)
        self.obstacles = obstacles

    def draw(self) -> None:
        begin_drawing()
        begin_mode_3d(self.camera.object)
        clear_background(WHITE)
        draw_grid(10, 2)
        for entity in self.entities():
            entity.draw()
        end_mode_3d()
        draw_fps(0, 0)
        end_drawing()

    def run(self) -> None:
        while not window_should_close():
            self.update(get_frame_time())
            self.draw()
        self.close()

    def entities(self) -> list[Entity]:
        return (
            [
                self.background,
                self.loader,
                self.camera,
                self.player,
            ]
            + self.obstacles
            + self.lasers
        )

    def add_obstacle(self):
        self.obstacles.append(Obstacle())

    def add_laser(self, position: Vector3):
        self.lasers.append(Laser(self.loader.get_model("laser"), position))


if __name__ == "__main__":
    game = Game()
    game.run()
