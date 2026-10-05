from pyray import (
    WHITE,
    begin_drawing,
    begin_mode_3d,
    clear_background,
    close_window,
    draw_grid,
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
        clear_background(WHITE)
        draw_grid(10, 2)
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
