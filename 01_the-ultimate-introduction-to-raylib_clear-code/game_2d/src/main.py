from pyray import (
    RED,
    clear_background,
    close_audio_device,
    draw_fps,
    end_drawing,
    get_frame_time,
    init_audio_device,
    init_window,
    is_window_resized,
    close_window,
    window_should_close,
    begin_drawing,
)

from core.config import BG_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT
from core.sprite import Sprite
from sprites.music import Music
from sprites.player import Player
from sprites.obstacle import Meteor, Obstacle
from sprites.weapon import Laser, Weapon


class Game:
    def __init__(self) -> None:
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Game 2D")
        init_audio_device()
        self.wait_for_window_size()
        self.obstacle = Obstacle()
        self.player = Player()
        self.sprites: list[Sprite] = [Music(), self.obstacle, self.player]

    def close(self) -> None:
        for sprite in self.sprites:
            sprite.close()
        close_audio_device()
        close_window()

    def update(self, delta_time: float) -> None:
        for laser in self.player.weapon.lasers:
            for meteor in self.obstacle.meteors:
                if (
                    meteor.position.x <= laser.position.x
                    and laser.position.x <= meteor.position.x + meteor.width
                ):
                    self.player.weapon.lasers.remove(laser)
                    self.obstacle.meteors.remove(meteor)

        for sprite in self.sprites:
            sprite.update(delta_time)

    def draw(self) -> None:
        begin_drawing()
        clear_background(BG_COLOR)
        draw_fps(0, 0)
        for sprite in self.sprites:
            sprite.draw()
        end_drawing()

    def wait_for_window_size(self) -> None:
        # Tiling WMs (Hyprland) resize the window only after the first frames are drawn
        for _ in range(10):
            begin_drawing()
            clear_background(RED)
            end_drawing()
            if is_window_resized():
                break

    def run(self) -> None:
        while not window_should_close():
            delta_time = get_frame_time()
            self.update(delta_time)
            self.draw()
        self.close()


if __name__ == "__main__":
    Game().run()
