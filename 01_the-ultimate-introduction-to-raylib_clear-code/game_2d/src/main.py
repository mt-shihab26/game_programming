from pyray import (
    Vector2,
    check_collision_recs,
    clear_background,
    close_audio_device,
    draw_fps,
    end_drawing,
    get_frame_time,
    init_audio_device,
    init_window,
    close_window,
    load_music_stream,
    load_sound,
    load_texture,
    unload_music_stream,
    unload_sound,
    unload_texture,
    window_should_close,
    begin_drawing,
)

from core.config import (
    BG_COLOR,
    MIN_METEOR_TIMER_DURATION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)
from core.entity import Entity
from core.paths import (
    laser_image_path,
    laser_sound_path,
    music_sound_path,
    spaceship_image_path,
    star_image_path,
)
from core.window import wait_for_window_size
from entities.counter import Counter
from entities.explosion import Explosion
from entities.background import Background
from sprites.laser import Laser
from sprites.player import Player
from entities.obstacle import Meteor, Obstacle


class Game:
    def load(self) -> None:
        self.textures = {
            "player": load_texture(spaceship_image_path()),
            "star": load_texture(star_image_path()),
            "laser": load_texture(laser_image_path()),
        }
        self.musics = {
            "background": load_music_stream(music_sound_path()),
        }
        self.sounds = {
            "laser": load_sound(laser_sound_path()),
        }

    def unload(self) -> None:
        for texture in self.textures.values():
            unload_texture(texture)
        for music in self.musics.values():
            unload_music_stream(music)
        for sound in self.sounds.values():
            unload_sound(sound)

    def __init__(self) -> None:
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Space shooter")
        init_audio_device()
        wait_for_window_size()

        self.load()

        self.background = Background(self.textures["star"], self.musics["background"])
        self.player = Player(self.textures["player"], self.shoot_laser)

        self.lasers: list[Laser] = []

        self.obstacle = Obstacle()
        self.counter = Counter()
        self.explosion = Explosion()

        self.sprites: list[Entity] = [
            self.obstacle,
            self.counter,
            self.explosion,
        ]

    def shoot_laser(self, position: Vector2):
        self.lasers.append(
            Laser(self.textures["laser"], self.sounds["laser"], position)
        )

    def close(self) -> None:
        self.background.close()
        self.player.close()

        for laser in self.lasers:
            laser.close()

        for sprite in self.sprites:
            sprite.close()

        self.unload()

        close_audio_device()
        close_window()

    def update(self, delta_time: float) -> None:
        self.handle_laser_meteor_collisions()
        self.handle_player_meteor_collisions()

        self.background.update(delta_time)
        self.player.update(delta_time)

        for laser in self.lasers:
            laser.update(delta_time)

        for sprite in self.sprites:
            sprite.update(delta_time)

    def handle_laser_meteor_collisions(self):
        remove_lasers_indexs: list[int] = []
        remove_meteors_indexs: list[int] = []
        for laser_index, laser in enumerate(self.lasers):
            for meteor_index, meteor in enumerate(self.obstacle.meteors):
                if meteor_index in remove_meteors_indexs:
                    continue
                if check_collision_recs(laser.rec(), meteor.rec()):
                    self.on_laser_hit_meteor(meteor.position)
                    remove_lasers_indexs.append(laser_index)
                    remove_meteors_indexs.append(meteor_index)
                    break

        lasers: list[Laser] = []
        for index, laser in enumerate(self.lasers):
            if index not in remove_lasers_indexs:
                lasers.append(laser)
        self.lasers = lasers

        meteors: list[Meteor] = []
        for index, meteor in enumerate(self.obstacle.meteors):
            if index not in remove_meteors_indexs:
                meteors.append(meteor)
        self.obstacle.meteors = meteors

    def handle_player_meteor_collisions(self):
        for meteor in self.obstacle.meteors:
            if check_collision_recs(self.player.rec(), meteor.rec()):
                pass

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

        self.background.draw()
        self.player.draw()

        for laser in self.lasers:
            laser.draw()

        for sprite in self.sprites:
            sprite.draw()

        end_drawing()

    def run(self) -> None:
        while not window_should_close():
            delta_time = get_frame_time()
            self.update(delta_time)
            self.draw()
        self.close()


if __name__ == "__main__":
    Game().run()
