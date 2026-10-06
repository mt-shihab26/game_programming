from pyray import play_music_stream, update_music_stream

from pyray import Music, Sound
from core.entity import Entity


class Background(Entity):
    def __init__(self, music: Music) -> None:
        self.music = music
        play_music_stream(music)

    def update(self, dt) -> None:
        update_music_stream(self.music)
