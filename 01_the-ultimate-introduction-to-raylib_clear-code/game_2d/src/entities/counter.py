from pyray import (
    WHITE,
    Font,
    Vector2,
    draw_text_ex,
    get_screen_height,
    get_screen_width,
    load_font_ex,
    measure_text_ex,
    unload_font,
)

from core.config import FONT_SIZE
from core.paths import stormfaze_font_path
from core.entity import Entity


class Counter(Entity):
    def __init__(self, font: Font) -> None:
        self.count = 0
        self.font = font

    def up(self):
        self.count += 1

    def draw(self) -> None:
        text = f"{self.count}"
        position = Vector2(
            int(
                (get_screen_width() - measure_text_ex(self.font, text, FONT_SIZE, 0).x)
                / 2
            ),
            int((get_screen_height() / 5) / 2),
        )
        draw_text_ex(self.font, text, position, FONT_SIZE, 0, WHITE)
