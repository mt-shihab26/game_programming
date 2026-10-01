from pyray import (
    WHITE,
    Vector2,
    draw_text,
    draw_text_ex,
    draw_text_pro,
    get_screen_height,
    get_screen_width,
    load_font,
    measure_text,
    unload_font,
)

from core.config import FONT_SIZE
from core.paths import stormfaze_font_path
from core.sprite import Sprite


class Counter(Sprite):
    def __init__(self) -> None:
        self.count = 0
        self.font = load_font(stormfaze_font_path())

    def up(self):
        self.count += 1

    def close(self) -> None:
        unload_font(self.font)

    def update(self, delta_time: float) -> None:
        pass

    def draw(self) -> None:
        text = f"{self.count}"
        draw_text_ex(
            self.font,
            text,
            Vector2(
                int((get_screen_width() - measure_text(text, FONT_SIZE)) / 2),
                int((get_screen_height() / 5) / 2),
            ),
            FONT_SIZE,
            0,
            WHITE,
        )
