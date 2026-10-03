from pyray import (
    Vector2,
    check_collision_circle_rec,
    check_collision_circles,
    check_collision_recs,
    clear_background,
    close_audio_device,
    draw_fps,
    end_drawing,
    get_frame_time,
    get_screen_height,
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
    MAX_METEOR_DURATION,
    MIN_METEOR_DURATION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)
from core.entity import Entity
from core.paths import (
    explosion_image_paths,
    explosion_sound_path,
    laser_image_path,
    laser_sound_path,
    meteor_image_path,
    music_sound_path,
    spaceship_image_path,
    star_image_path,
)
from core.timer import Timer
from core.window import wait_for_window_size
from entities.counter import Counter
from entities.background import Background
from sprites.explosion import Explosion2
from sprites.laser import Laser
from sprites.meteor import Meteor
from sprites.player import Player


class Game:
    def load(self) -> None:
        self.textures = {
            "player": load_texture(spaceship_image_path()),
            "star": load_texture(star_image_path()),
            "laser": load_texture(laser_image_path()),
            "meteor": load_texture(meteor_image_path()),
            "explosion": [load_texture(path) for path in explosion_image_paths()],
        }

        self.musics = {
            "background": load_music_stream(music_sound_path()),
        }
        self.sounds = {
            "laser": load_sound(laser_sound_path()),
            "explosion": load_sound(explosion_sound_path()),
        }

    def unload(self) -> None:
        for texture in self.textures.values():
            if isinstance(texture, list):
                for frame in texture:
                    unload_texture(frame)
            else:
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

        self.lasers: list[Laser] = []
        self.meteors: list[Meteor] = []
        self.explosions: list[Explosion2] = []

        self.background = Background(self.textures["star"], self.musics["background"])
        self.player = Player(self.textures["player"], self.add_laser)

        self.meteor_timer = Timer(MAX_METEOR_DURATION, True, True, self.add_meteor)

        self.counter = Counter()

        self.sprites: list[Entity] = [
            self.counter,
        ]

    def entities(self) -> list[Entity]:
        return (
            [
                self.background,
                self.player,
            ]
            + self.lasers
            + self.meteors
            + self.sprites
            + self.explosions
        )

    def add_laser(self, position: Vector2):
        texture = self.textures["laser"]
        sound = self.sounds["laser"]
        self.lasers.append(Laser(texture, sound, position))

    def add_meteor(self):
        texture = self.textures["meteor"]
        self.meteors.append(Meteor(texture))

    def add_explosion(self, position: Vector2):
        textures = self.textures["explosion"]
        sound = self.sounds["explosion"]
        self.explosions.append(Explosion2(textures, position, sound))

    def close(self) -> None:
        for entity in self.entities():
            entity.close()

        self.unload()

        close_audio_device()
        close_window()

    def update(self, delta_time: float) -> None:
        self.handle_laser_meteor_collisions()
        self.handle_player_meteor_collisions()
        self.handle_remove_lasers_out_of_screen()
        self.handle_remove_meteors_out_of_screen()
        self.handle_remove_explosions_out_of_screen()

        self.meteor_timer.update()

        for entity in self.entities():
            entity.update(delta_time)

    def handle_laser_meteor_collisions(self):
        for laser in self.lasers[:]:
            for meteor in self.meteors:
                if check_collision_circle_rec(
                    meteor.center(),
                    meteor.radius,
                    laser.rectangle(),
                ):
                    self.add_explosion(meteor.position)
                    self.on_laser_hit_meteor(meteor.position)
                    self.lasers.remove(laser)
                    self.meteors.remove(meteor)
                    break

    def on_laser_hit_meteor(self, position: Vector2):
        self.counter.up()

        if (
            0 < self.counter.count
            and self.counter.count % 4 == 0
            and MIN_METEOR_DURATION < self.meteor_timer.duration
        ):
            self.meteor_timer.duration = round(self.meteor_timer.duration - 0.1, 1)

    def handle_player_meteor_collisions(self):
        for meteor in self.meteors:
            if check_collision_circles(
                self.player.center(), self.player.radius, meteor.center(), meteor.radius
            ):
                pass

    def handle_remove_lasers_out_of_screen(self):
        self.lasers = [laser for laser in self.lasers if laser.position.y >= 0]

    def handle_remove_meteors_out_of_screen(self):
        h = get_screen_height()
        self.meteors = [meteor for meteor in self.meteors if meteor.position.y <= h]

    def handle_remove_explosions_out_of_screen(self):
        self.explosions = [
            explosion
            for explosion in self.explosions
            if explosion.index < explosion.len
        ]

    def draw(self) -> None:
        begin_drawing()
        clear_background(BG_COLOR)
        draw_fps(0, 0)

        for entity in self.entities():
            entity.draw()

        end_drawing()

    def run(self) -> None:
        while not window_should_close():
            delta_time = get_frame_time()
            self.update(delta_time)
            self.draw()
        self.close()


if __name__ == "__main__":
    Game().run()
