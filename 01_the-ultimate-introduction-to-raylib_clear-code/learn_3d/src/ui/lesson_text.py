from pyray import draw_text

from pyray import BLACK, DARKBLUE, DARKGRAY
from core.lessons import LESSONS


class LessonText:
    def draw(self, lesson: int) -> None:
        title, lines, keys = LESSONS[lesson]
        draw_text(f"{lesson + 1}/{len(LESSONS)}  {title}", 20, 20, 30, BLACK)
        for i, line in enumerate(lines):
            draw_text(line, 20, 64 + i * 26, 20, DARKGRAY)
        draw_text(keys, 20, 76 + len(lines) * 26, 20, DARKBLUE)
