from pyray import ffi, load_font_ex, load_music_stream, load_sound, load_texture
from pyray import unload_font, unload_music_stream, unload_sound, unload_texture
from core.paths import explosion_image_paths, explosion_sound_path, laser_image_path
from core.paths import laser_sound_path, meteor_image_path, music_sound_path
from core.paths import spaceship_image_path, star_image_path, stormfaze_font_path

from core.config import FONT_SIZE


class Loader:
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
        self.fonts = {
            "stormfaze": load_font_ex(stormfaze_font_path(), FONT_SIZE, ffi.NULL, 0),
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
        for font in self.fonts.values():
            unload_font(font)
