from pyray import (
    begin_drawing,
    begin_mode_3d,
    close_window,
    end_drawing,
    end_mode_3d,
    init_window,
    window_should_close,
)

from camera import Camera


class Game:
    def __init__(self) -> None:
        self.camera = Camera()

        self.init()

    def init(self) -> None:
        init_window(1220, 680, "Game 3D")

    def close(self):
        close_window()

    def update(self):
        pass

    def draw(self):
        begin_drawing()
        begin_mode_3d(self.camera.object)
        end_mode_3d()
        end_drawing()

    def run(self) -> None:
        while not window_should_close():
            self.update()
            self.draw()
        self.close()


if __name__ == "__main__":
    game = Game()
    game.run()
