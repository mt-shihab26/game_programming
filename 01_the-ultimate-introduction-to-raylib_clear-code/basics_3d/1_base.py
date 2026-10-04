from pyray import *
from raylib import *

init_window(1920, 1080, "3D base")

while not window_should_close():
    dt = get_frame_time()
    clear_background(WHITE)
    begin_drawing()
    end_drawing()
close_window()