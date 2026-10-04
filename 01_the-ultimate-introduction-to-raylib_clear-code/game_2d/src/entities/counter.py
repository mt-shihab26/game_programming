from pyray import (
    WHITE,
    Font,
    Vector2,
    draw_text_ex,
    get_screen_height,
    get_screen_width,
    measure_text_ex,
)

from core.config import FONT_SIZE
from core.entity import Entity


class Counter(Entity):
    def __init__(self, font: Font) -> None:
        self.count = 0
        self.font = font

    def up(self):
        self.count += 1

    def draw(self) -> None:
        text_content = f"{self.count}"
        text_size = measure_text_ex(self.font, text_content, FONT_SIZE, 0).x
        position = Vector2(
            int((get_screen_width() - text_size) / 2),
            int((get_screen_height() / 5) / 2),
        )
        draw_text_ex(self.font, text_content, position, FONT_SIZE, 0, WHITE)
