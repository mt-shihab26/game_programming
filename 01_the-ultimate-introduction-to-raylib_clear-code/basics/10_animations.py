from pyray import *
from os.path import join

init_window(1000, 600, "Animations")

animations_frames = [
    load_texture(join("assets", "animation", f"{i}.png")) for i in range(8)
]
animations_index = 0
animations_speed = 8

while not window_should_close():
    delta_time = get_frame_time()

    animations_index += animations_speed * delta_time

    if len(animations_frames) <= animations_index:
        animations_index = 0

    begin_drawing()
    clear_background(WHITE)
    draw_texture(animations_frames[int(animations_index)], 400, 260, WHITE)
    end_drawing()

for frame in animations_frames:
    unload_texture(frame)

close_window()
