from pyray import (
    RED,
    Vector2,
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

from core.config import (
    BG_COLOR,
    MIN_METEOR_TIMER_DURATION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)
from core.sprite import Sprite
from sprites.counter import Counter
from sprites.explosion import Explosion
from sprites.background import Background
from sprites.player import Player
from sprites.obstacle import Meteor, Obstacle
from sprites.weapon import Laser


class Game:
    def __init__(self) -> None:
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Space shooter")
        init_audio_device()
        self.wait_for_window_size()
        self.obstacle = Obstacle()
        self.player = Player()
        self.counter = Counter()
        self.explosion = Explosion()

        self.sprites: list[Sprite] = [
            Background(),
            self.obstacle,
            self.player,
            self.counter,
            self.explosion,
        ]

    def close(self) -> None:
        for sprite in self.sprites:
            sprite.close()
        close_audio_device()
        close_window()

    def run(self) -> None:
        while not window_should_close():
            delta_time = get_frame_time()
            self.update(delta_time)
            self.draw()
        self.close()

    def update(self, delta_time: float) -> None:
        self.handle_laser_meteor_collisions()
        for sprite in self.sprites:
            sprite.update(delta_time)

    def handle_laser_meteor_collisions(self):
        remove_lasers_indexs: list[int] = []
        remove_meteors_indexs: list[int] = []
        for laser_index, laser in enumerate(self.player.weapon.lasers):
            for meteor_index, meteor in enumerate(self.obstacle.meteors):
                y_position_collision = (
                    laser.position.y + self.player.weapon.texture.height
                    < meteor.position.y + (self.obstacle.texture.height / 3)
                )
                x_position_collision = (
                    meteor.position.x <= laser.position.x
                    and laser.position.x + self.player.weapon.texture.width
                    <= meteor.position.x + self.obstacle.texture.width
                )
                if y_position_collision and x_position_collision:
                    self.on_laser_hit_meteor(meteor.position)
                    remove_lasers_indexs.append(laser_index)
                    remove_meteors_indexs.append(meteor_index)

        lasers: list[Laser] = []
        for index, laser in enumerate(self.player.weapon.lasers):
            try:
                x = remove_lasers_indexs.index(index)
            except:
                lasers.append(laser)
        self.player.weapon.lasers = lasers

        meteors: list[Meteor] = []
        for index, meteor in enumerate(self.obstacle.meteors):
            try:
                x = remove_meteors_indexs.index(index)
            except:
                meteors.append(meteor)
        self.obstacle.meteors = meteors

    def on_laser_hit_meteor(self, position: Vector2):
        self.counter.up()
        self.explosion.add(
            Vector2(
                position.x + (self.obstacle.texture.width / 2),
                position.y + (self.obstacle.texture.height / 2),
            )
        )
        if (
            0 < self.counter.count
            and self.counter.count % 4 == 0
            and MIN_METEOR_TIMER_DURATION < self.obstacle.timer.duration
        ):
            self.obstacle.timer.duration = round(self.obstacle.timer.duration - 0.1, 1)

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


if __name__ == "__main__":
    Game().run()
