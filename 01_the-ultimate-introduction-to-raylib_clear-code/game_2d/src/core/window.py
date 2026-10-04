from pyray import begin_drawing, clear_background, end_drawing, is_window_resized

from pyray import RED


def wait_for_window_size() -> None:
    # Tiling WMs (Hyprland) resize the window only after the first frames are drawn
    for _ in range(10):
        begin_drawing()
        clear_background(RED)
        end_drawing()
        if is_window_resized():
            break
