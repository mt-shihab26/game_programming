from pyray import close_window, init_window, window_should_close


class Game:
    def __init__(self) -> None:
        self.init()

    def init(self) -> None:
        init_window(1220, 680, "Game 3D")

    def close(self):
        close_window()

    def update(self):
        pass

    def draw(self):
        pass

    def run(self) -> None:
        while not window_should_close():
            self.update()
            self.draw()
        self.close()


if __name__ == "__main__":
    game = Game()
    game.run()
