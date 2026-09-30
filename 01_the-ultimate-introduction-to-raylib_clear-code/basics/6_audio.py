from pyray import *
from os.path import join


init_window(1000, 600, "Audio")
init_audio_device()


laser_sound = load_sound(join("assets", "laser.wav"))
music_stream = load_music_stream(join("assets", "music.wav"))


play_sound(laser_sound)
play_music_stream(music_stream)


while not window_should_close():
    update_music_stream(music_stream)

    begin_drawing()
    clear_background(BLACK)

    end_drawing()


unload_music_stream(music_stream)
close_audio_device()
close_window()
