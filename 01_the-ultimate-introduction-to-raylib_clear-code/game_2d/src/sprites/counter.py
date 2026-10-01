from pyray import WHITE, draw_text, get_screen_height, get_screen_width, measure_text

from core.config import FONT_SIZE
from core.sprite import Sprite


class Counter(Sprite):
    def __init__(self) -> None:
        self.count = 0

    def close(self) -> None:
        pass

    def update(self, delta_time: float) -> None:
        pass

    def draw(self) -> None:
        text = f"{self.count}"
        draw_text(
            text,
            int((get_screen_width() - measure_text(text, FONT_SIZE)) / 2),
            int((get_screen_height() / 5) / 2),
            FONT_SIZE,
            WHITE,
        )
