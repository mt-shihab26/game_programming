from pyray import (
    load_audio_stream,
    load_music_stream,
    unload_music_stream,
    update_music_stream,
)
from os.path import join

from core.sprite import Sprite


class Music(Sprite):
    def __init__(self) -> None:
        self.stream = load_music_stream(join("assets", "sounds", "music.wav"))

    def deinit(self) -> None:
        unload_music_stream(self.stream)

    def update(self, delta_time: float) -> None:
        update_music_stream(self.stream)

    def draw(self) -> None:
        pass
