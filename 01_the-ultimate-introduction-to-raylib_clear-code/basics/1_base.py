from pyray import *
from os.path import join

init_window(1000, 600, "Hello World")

spaceship_texture = load_texture(join("assets", "spaceship.png"))

cowboy_image = load_image(join("assets", "animation", "0.png"))
image_color_invert(cowboy_image)
cowboy_texture = load_texture_from_image(cowboy_image)

font = load_font(join("assets", "zero-hour.otf"))

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)

    draw_line_ex(Vector2(0, 0), Vector2(500, 200), 10, (255, 0, 0, 255))
    draw_texture(spaceship_texture, 0, 0, WHITE)
    draw_texture(cowboy_texture, 1000, 600, WHITE)

    draw_text("Some text", 0, 300, 100, WHITE)
    draw_text_ex(font, "Some text", Vector2(0, 400), 100, 0, WHITE)

    end_drawing()

unload_image(cowboy_image)
unload_texture(spaceship_texture)

close_window()
